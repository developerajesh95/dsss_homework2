import unittest
from math_quiz import getRandomIntFromRange, operatorSelection, performOperation


class TestMathGame(unittest.TestCase):

    def test_getRandomIntFromRange(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomIntFromRange(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operatorSelection(self):
        # test for random generated operator
        operators = ['+', '-', '*']
        for _ in range(1000):
             rand_operator = operatorSelection()
             self.assertTrue(rand_operator, operators)
        pass

    def test_performOperation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 6, '*', '6 * 6', 36),
                (8, 6, '-', '8 - 6', 2),
                (9, 7, '+', '9 + 7', 16),
                (4, 7, '*', '4 * 7', 28),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                test_question, test_answer = performOperation(num1, num2, operator)

                #check if the result matches with expected result
                self.assertEqual(test_question, expected_problem)
                self.assertEqual(test_answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
