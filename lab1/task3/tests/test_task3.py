import time, tracemalloc
import unittest
from lab1.task3.src.task3 import bin_sum


class TestMegreSort(unittest.TestCase):

    def test_should_merge_sort(self):
        # given
        array = [2, 1, 4, 6, 0]
        A = '0110110'
        B = '0100010'
        must_C = '1011000'
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        C = bin_sum(A, B)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(C, must_C)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
