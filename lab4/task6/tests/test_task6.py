import time, tracemalloc
import unittest
from lab3.task6.src.task6 import task6


class TestTask6(unittest.TestCase):

    def test_should_task6(self):
        # given
        array_a = [7, 1, 4, 9]
        array_b = [2, 7, 8, 11]
        right_answer = 51
        time_limit = 2
        memory_limit = 512

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        sorted_array = task6(array_a, array_b)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(sorted_array, right_answer)
        self.assertLessEqual(time_spent, time_limit)
        self.assertLessEqual(memory_used_in_mb, memory_limit)
