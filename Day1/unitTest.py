import unittest

class ArithmeticOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero")
        return self.x / self.y

class TestArithmeticOperations(unittest.TestCase):
    def setUp(self):
        self.obj = ArithmeticOperations(10, 5)

    def test_addition(self):
        self.assertEqual(self.obj.add(), 15)

    def test_subtraction(self):
        self.assertEqual(self.obj.subtract(), 5)

    def test_multiplication(self):
        self.assertEqual(self.obj.multiply(), 50)

    def test_division(self):
        self.assertEqual(self.obj.divide(), 2)

    def test_division_by_zero(self):
        obj_zero = ArithmeticOperations(10, 0)
        with self.assertRaises(ValueError):
            obj_zero.divide()

    def test_verify_x_and_y_values(self):
        self.assertEqual(self.obj.x, 10)
        self.assertEqual(self.obj.y, 5)

if __name__ == '__main__':
    unittest.main()