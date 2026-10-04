import unittest


class TestHealth(unittest.TestCase):
    def test_app_is_alive(self):
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
