import time, tracemalloc
import unittest
from lab4.task1.src.task1 import get_stack_deletions


class TestTask1(unittest.TestCase):

    def test_should_get_stack_deletions(self):
        # given
        commands = ['3', '-', '6', '182', '5', '-', '-', '99', '-']
        exception_deletions = ['3', '5', '182', '99']
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        deletions = get_stack_deletions(commands)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(deletions, exception_deletions)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)

        print(time_spent, memory_used_in_mb)
