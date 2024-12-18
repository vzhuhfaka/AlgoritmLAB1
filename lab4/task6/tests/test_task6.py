import time, tracemalloc
import unittest
from lab4.task6.src.task6 import get_queue_minimals


class TestTask6(unittest.TestCase):

    def test_should_get_queue_minimals(self):
        # given
        commands_format = ['8', '10', '?', '-', '2', '?', '1', '-', '?']
        exception_result = ['8', '2', '1']
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = get_queue_minimals(commands_format)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)
