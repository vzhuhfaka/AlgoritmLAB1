import unittest
from lab1.task2.src.linearfinder import linearfinder
from lab1.utils import txt_to_numlist


class TestLinearFinder(unittest.TestCase):

    def test_linearfinder(self):
        linearfinder('Lab1/task2/txtf/test_input.txt', 'Lab1/task2/txtf/test_output.txt')
        self.assertEqual(txt_to_numlist('Lab1/task2/txtf/test_output.txt'), ['3', '9'])
