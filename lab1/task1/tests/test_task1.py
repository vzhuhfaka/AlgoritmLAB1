import time, tracemalloc
import unittest
from lab1.task1.src.task1 import insertionsort


class TestInsertionSort(unittest.TestCase):

    def test_should_insertion_sort(self):
        # given
        array = [2, 1, 4, 6, 0]
        must_be_array = [0, 1, 2, 4, 6]
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        sorted_array = insertionsort(array)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(sorted_array, must_be_array)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
