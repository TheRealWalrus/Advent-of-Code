import unittest
import day_03_2 as solution


class TestSolution(unittest.TestCase):
    def test_solve(self):
        input_data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
        ]
        expected = 230

        actual = solution.solve(input_data)

        self.assertEqual(expected, actual)
