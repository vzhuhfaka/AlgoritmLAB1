import unittest
from lab1.task3.src.task3 import main_binsum
from lab1.utils import txt_to_str


class TestBinSum(unittest.TestCase):

    def test_binsum(self):
        main_binsum('lab1/task3/txtf/test_input.txt', 'lab1/task3/txtf/test_output.txt', 'lab1/task3/txtf/test_time.txt')
        self.assertEqual(txt_to_str('lab1/task3/txtf/test_output.txt'), '11101')
