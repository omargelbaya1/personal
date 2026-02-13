import unittest

# ----- code to test -----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

# ----- unit tests -----
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
