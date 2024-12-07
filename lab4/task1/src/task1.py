from lab3.utils import read_lines, write_in_file
import random


def task1(array: list) -> list:
    if len(array) <= 1:
        return array

    elem = random.choice(array)
    left = []
    center = []
    right = []

    for i in array:
        if i < elem:
            left.append(i)
        elif i == elem:
            center.append(i)
        else:
            right.append(i)

    return task1(left) + center + task1(right)


if __name__ == '__main__':
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array = read_lines(path_input)[1]  # берём вторую строчку, так как в первой число элементов
    sorted_array = task1(array)

    write_in_file(path_output, sorted_array)
    print(sorted_array)
