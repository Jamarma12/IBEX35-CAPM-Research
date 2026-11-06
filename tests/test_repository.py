"""Pruebas de integridad que no precisan conexión a Internet."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("capm_validate", ROOT / "scripts" / "validate_repository.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class TestRepository(unittest.TestCase):
    def test_notebook_and_csv(self):
        module.validate()

    def test_monthly_returns(self):
        prices = module.load_csv()
        monthly = prices.resample("ME").last().loc[:"2026-10-31"]
        ret = monthly.pct_change(fill_method=None).dropna()
        self.assertEqual(len(monthly), 145)
        self.assertEqual(len(ret), 144)
        self.assertFalse(ret.isna().any())
        self.assertAlmostEqual(monthly.loc["2014-12-31"], 24469.9, places=1)
        self.assertAlmostEqual(monthly.loc["2026-09-30"], 72298.9, places=1)


if __name__ == "__main__":
    unittest.main()
