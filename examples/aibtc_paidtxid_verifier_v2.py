"""Verify AIBTC paid flags against public Hiro transaction records."""
from __future__ import annotations
import json, sys, urllib.request, urllib.error, time
from pathlib import Path

BASE = "https://aibtc.com/api/bounties"
HIRO = "https://api.hiro.so/extended/v1/tx/"
EXPECTED_CONTRACT = "SM3VDXK3WZZSA84XXFKAFAF15NNZX32CTSG82JFQ4.sbtc-token"

def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Dana-Agent-Continuity-Kit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def main():
    rows=[]; offset=0
    while True:
        page=get(f"{BASE}?status=paid&limit=100&offset={offset}")
        batch=page.get("bounties", [])
        rows.extend(batch)
        if not page.get("hasMore") or not batch: break
        offset=page.get("nextOffset", offset+len(batch))
    out=[]
    for b in rows:
        txid=(b.get("paidTxid") or "").removeprefix("0x")
        item={"bounty_id":b.get("id"),"reward_sats":b.get("rewardSats"),"paid_txid":b.get("paidTxid"),"poster_stx":b.get("posterStxAddress"),"status":b.get("status")}
        if not txid:
            item.update(result="no_txid", evidence_url=None); out.append(item); continue
        item["evidence_url"]=HIRO+txid
        # The listing omits the winner; resolve the accepted submission from detail.
        try:
            detail=get(BASE+"/"+b["id"])
            winner=detail.get("winner") or {}
            b["winnerStxAddress"]=winner.get("submitterStxAddress") if winner.get("submissionId") == b.get("acceptedSubmissionId") and b.get("acceptedSubmissionId") else None
            item["winner_stx"]=b["winnerStxAddress"]
            item["winner_source"]=BASE+"/"+b["id"]
        except (urllib.error.URLError, TimeoutError) as error:
            item.update(result="unverifiable", error="Winner lookup: " + str(error)); out.append(item); continue
        time.sleep(1)
        try: tx=get(HIRO+txid)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # Public endpoint throttles bursts. One bounded retry keeps the
                # result honest without hammering the service.
                time.sleep(2)
                try: tx=get(HIRO+txid)
                except urllib.error.HTTPError as retry_error:
                    item.update(result="unverifiable", error=f"HTTP {retry_error.code}"); out.append(item); continue
            else:
                item.update(result="unverifiable", error=f"HTTP {e.code}"); out.append(item); continue
        item.update(hiro_status=tx.get("tx_status"), tx_type=tx.get("tx_type"))
        call=tx.get("contract_call") or {}; args={a.get("name"):a.get("repr","") for a in call.get("function_args",[])}
        amount=args.get("amount","").removeprefix("u")
        recipient=args.get("recipient","").removeprefix("'")
        memo=args.get("memo","")
        # Hiro returns optional buff values as `(some 0x...)`; decode the
        # bytes before checking the protocol's BNTY:<id> memo.
        memo_text=memo
        if "0x" in memo:
            try: memo_text=bytes.fromhex(memo.split("0x",1)[1].rstrip(")")).decode("utf-8")
            except (ValueError, UnicodeDecodeError): pass
        memo_ok=bool(b.get("id")) and memo_text == "BNTY:" + b["id"]
        amount_ok=(str(b.get("rewardSats"))==amount)
        recipient_ok=bool(b.get("winnerStxAddress")) and b["winnerStxAddress"] == recipient
        item.update(contract=call.get("contract_id"),function=call.get("function_name"),amount_repr=amount,memo_repr=memo,memo_text=memo_text,recipient_repr=recipient,amount_matches=amount_ok,memo_matches=memo_ok,recipient_matches=recipient_ok,result="verified_transfer" if tx.get("tx_status")=="success" and call.get("function_name")=="transfer" and amount_ok and memo_ok and recipient_ok else "tx_found_inconclusive")
        item["contract_matches"] = call.get("contract_id") == EXPECTED_CONTRACT
        if not item["contract_matches"]:
            item["result"] = "tx_found_inconclusive"
        out.append(item)
    summary={"checked_at_utc":__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),"source":BASE+"?status=paid","hiro_source":HIRO,"count":len(out),"counts":{},"rows":out}
    for r in out: summary["counts"][r["result"]]=summary["counts"].get(r["result"],0)+1
    stamp=__import__('datetime').datetime.now(__import__('datetime').timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    path=Path(__file__).with_name("aibtc_paidtxid_verifier."+stamp+".json"); path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"result_file":str(path),"count":len(out),"counts":summary["counts"]}))
if __name__ == "__main__": main()

