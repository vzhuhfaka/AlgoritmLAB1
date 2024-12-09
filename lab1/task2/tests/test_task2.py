import time, tracemalloc
import unittest
from lab1.task2.src.task2 import linearfinder


class TestMegreSort(unittest.TestCase):

    def test_should_merge_sort(self):
        # given
        array = [2, 2, 4, 6, 0, 2]
        need_to_find = 2
        must_found_n = [0, 1, 5]
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        found_n = linearfinder(array, need_to_find)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(found_n, must_found_n)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
