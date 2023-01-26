import unittest
import main

input_date = 50
output_date = 18


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = main.euler(input_date)
        self.assertEqual(result, output_date)


if __name__ == '__main__':
    unittest.main()
