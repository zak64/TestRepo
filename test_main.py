import unittest

from main import f1


class TestF1(unittest.TestCase):
    def test_returns_input_when_non_zero(self):
        self.assertEqual(f1(5), 5)

    def test_raises_exception_when_zero(self):
        with self.assertRaises(Exception) as context:
            f1(0)
        self.assertIn("inoput a not valid is 0", str(context.exception))


if __name__ == "__main__":
    unittest.main()
