import time, tracemalloc
import unittest
from lab3.task1.src.task1 import task1


class TestTask1(unittest.TestCase):

    def test_should_quick_sort(self):
        # given
        array = [4, 6, 77, 1, 0, 1, 1, 1]
        must_be_array = [0, 1, 1, 1, 1, 4, 6, 77]
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        sorted_array = task1(array)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(sorted_array, must_be_array)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
