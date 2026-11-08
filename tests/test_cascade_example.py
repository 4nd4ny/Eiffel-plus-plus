"""Le démonstrateur public doit exercer les trois passages, sans vrai accord humain."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cascade_example", ROOT / "examples/cascade-0.7.0/demo.py")
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)


class CascadeExampleTests(unittest.TestCase):
    def test_public_example_stays_explicitly_synthetic_and_finishes_all_levels(self):
        with tempfile.TemporaryDirectory() as root:
            destination = Path(root) / "demo"
            result = demo.run(destination)
            self.assertEqual(result["human_review"], "SIMULATED_FOR_TEST_ONLY")
            self.assertEqual([row["level"] for row in result["levels"]], [2, 1, 0])
            self.assertTrue(all(row["before"] == "INCONCLUSIVE" and row["after"] == "READY" for row in result["levels"]))
            self.assertEqual(result["journal"]["verdict"], "PASS")
            self.assertTrue(result["journal"]["completed"])
            self.assertEqual(json.loads((destination / "result.json").read_text()), result)


if __name__ == "__main__":
    unittest.main()
