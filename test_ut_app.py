"""Test App Unittest"""

import unittest
import app


class TestApp(unittest.TestCase):
    """Test App using unittest"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        """Test function add"""
        self.assertEqual(3, app.add(1))


if __name__ == "__main__":
    unittest.main()
