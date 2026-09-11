import unittest

from continuity_audit import audit


class AuditEvidenceTests(unittest.TestCase):
    def test_distinct_receipts_do_not_prove_distinct_actions(self):
        result = audit({
            "objective": "synthetic replay",
            "recovery_bundle": {"version": 1},
            "events": [{"id": "e1", "action": "send"}, {"id": "e2", "action": "send"}],
            "permissions": [{"action": "send", "active": True}],
            "receipts": [{"id": "r1", "action_key": "same"}, {"id": "r2", "action_key": "same"}],
        })
        checks = {check["name"]: check for check in result["checks"]}
        self.assertTrue(checks["receipt_ids_unique"]["passed"])
        self.assertNotIn("receipts_prevent_duplicate_actions", checks)
        self.assertIn("do not prove", result["limitations"][1])
        self.assertFalse(result["input_secret_scan_performed"])
        self.assertNotIn("secret_free", result)

    def test_duplicate_receipt_ids_fail(self):
        result = audit({"receipts": [{"id": "r1"}, {"id": "r1"}]})
        checks = {check["name"]: check for check in result["checks"]}
        self.assertFalse(checks["receipt_ids_unique"]["passed"])


if __name__ == "__main__":
    unittest.main()
