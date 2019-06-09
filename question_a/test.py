import unittest
import main as question_a

class QuestionATest(unittest.TestCase):
       
    def test_must_check_if_there_is_an_overlap(self):
        l1 = (1,10)
        l2=(22,7)
        res = question_a.check_overlap(l1,l2)
        self.assertTrue(res)

    def test_must_check_if_there_is_no_overlap(self):
        l1 = (1,10)
        l2=(11,22)
        res = question_a.check_overlap(l1,l2)
        self.assertFalse(res)

           