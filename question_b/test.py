import unittest
import main as question_b


# Question B
# The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, 
# or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

class TestQuestionB(unittest.TestCase):

    def setUp(self):
        self.greater_value="9.5"
        self.value="3.0"
        self.expected = f"{self.greater_value} > {self.value}"
    def test_must_return_first_value_is_greater(self):
        actual = question_b.check_values(self.greater_value, self.value)
        self.assertEqual(self.expected, actual)

    def test_must_return_second_value_is_greater(self):
        actual = question_b.check_values(self.value, self.greater_value)
        self.assertEqual(self.expected, actual)

    def test_must_return_values_are_equal(self):
        val1, val2 = (1,1)
        expected = f"1.0 equals 1.0"
        actual = question_b.check_values(val1,val2)
        self.assertEqual(expected, actual)

    def test_must_handle_value_error(self):
        expected = "gimme numbers plz"
        actual = question_b.check_values("abc", None)
        self.assertEqual(expected, actual)