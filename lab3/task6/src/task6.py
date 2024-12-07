from lab3.utils import read_lines, write_in_file
from lab3.task1.src.task1 import task1 as qsort


def combinations(A: list, B: list) -> list:
    res = []
    for a in A:
        for b in B:
            res.append(a * b)
    return res


def sum_tenth(array: list) -> int:
    res = 0
    for i in range(0, len(array), 10):
        res += array[i]
    return res


def task6(A: list, B: list) -> int:
    C = qsort(combinations(A, B))  # сортируем массив, состоящий из произведений элементов списков A и B
    answer = sum_tenth(C)
    return answer


if __name__ == '__main__':
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array_a = read_lines(path_input)[1]  # берём вторую строчку, так как в первой число элементов
    array_b = read_lines(path_input)[2]  # берём вторую строчку, так как в первой число элементов

    res = task6(array_a, array_b)

    write_in_file(path_output, res)
    print(res)
