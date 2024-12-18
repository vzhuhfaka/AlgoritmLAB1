import time, tracemalloc
import unittest
from lab4.task11.src.task11 import get_rest


class TestTask11(unittest.TestCase):

    def test_should_get_rest(self):
        # given
        data = ['5', '1', '76', '3', '1']
        certificates = 7
        exception_result = [3, 75, 1]
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = get_rest(data, certificates)[1]

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)
