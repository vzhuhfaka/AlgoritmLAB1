import unittest
import time, tracemalloc
from lab2.task5.src.task5 import majority



class TestBinSearch(unittest.TestCase):

    def test_task5(self):
        # given
        array = [2, 4, 2, 2, 3]
        must_be_result = 1
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = majority(array)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, must_be_result)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)

