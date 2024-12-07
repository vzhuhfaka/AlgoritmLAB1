import time, tracemalloc
import unittest
from lab2.task4.src.task4 import BinSearch


class TestBinSearch(unittest.TestCase):

    def test_should_bin_search(self):
        # given
        array = [1, 5, 8, 12, 13]
        to_search_n = [8, 1, 23, 1, 11]
        must_be_array = [2, 0, -1, 0, -1]
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        found_n = []
        for i in to_search_n:
            found_n.append(BinSearch(array, i))

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(found_n, must_be_array)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
