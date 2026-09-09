"""Offline regression checks; these do not establish on-chain payment facts."""
import contextlib
import copy
import io
import json
import unittest
from unittest.mock import patch
import aibtc_paidtxid_verifier_v2 as verifier


class PaymentChecks(unittest.TestCase):
    def classify(self, change=None, missing_winner=False, contract=verifier.EXPECTED_CONTRACT):
        bounty = {"id": "sample", "rewardSats": 100, "paidTxid": "0xtest", "acceptedSubmissionId": "accepted", "winnerStxAddress": "SPWINNER"}
        if missing_winner:
            bounty.pop("winnerStxAddress")
        args = {"amount": "u100", "recipient": "'SPWINNER", "memo": "(some 0x" + b"BNTY:sample".hex() + ")"}
        if change:
            args.update(change)
        tx = {"tx_status": "success", "contract_call": {"function_name": "transfer", "function_args": [{"name": k, "repr": v} for k, v in args.items()]}}
        tx["contract_call"]["contract_id"] = contract
        detail={"winner": {"submissionId": "accepted", "submitterStxAddress": bounty.get("winnerStxAddress")}}
        with patch.object(verifier, "get", side_effect=[{"bounties": [bounty]}, detail, tx]), patch.object(verifier.time, "sleep"), patch.object(verifier.Path, "write_text") as output, contextlib.redirect_stdout(io.StringIO()):
            verifier.main()
        return json.loads(output.call_args.args[0])["rows"][0]["result"]

    def test_matching_fields(self):
        self.assertEqual(self.classify(), "verified_transfer")

    def test_wrong_recipient(self):
        self.assertEqual(self.classify({"recipient": "'SPOTHER"}), "tx_found_inconclusive")

    def test_wrong_contract(self):
        self.assertEqual(self.classify(contract="SPOTHER.fake-token"), "tx_found_inconclusive")

    def test_missing_contract(self):
        self.assertEqual(self.classify(contract=None), "tx_found_inconclusive")

    def test_missing_winner(self):
        self.assertEqual(self.classify(missing_winner=True), "tx_found_inconclusive")

    def test_wrong_amount(self):
        self.assertEqual(self.classify({"amount": "u101"}), "tx_found_inconclusive")

    def test_memo_substring_is_insufficient(self):
        self.assertEqual(self.classify({"memo": "BNTY:sample-other"}), "tx_found_inconclusive")

    def test_wrong_memo(self):
        self.assertEqual(self.classify({"memo": "BNTY:other"}), "tx_found_inconclusive")


if __name__ == "__main__":
    unittest.main()

