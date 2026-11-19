import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("DevOps"),
            "Hello, DevOps! CI/CD is working!"
        )

if __name__ == "__main__":
    unittest.main()
