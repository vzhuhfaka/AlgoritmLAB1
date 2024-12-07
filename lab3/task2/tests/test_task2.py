import time, tracemalloc
import unittest
from lab3.task2.src.task2 import task2


class TestTask2(unittest.TestCase):

    def test_should_task2(self):
        # given
        n = 10
        must_be_array = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]
        time_limit = 2
        memory_limit = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        worst_array = task2(n)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(worst_array, must_be_array)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
