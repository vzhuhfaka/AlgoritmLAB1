from lab3.utils import read_lines, write_in_file


def task2(n:int ) -> list:
    a = [i for i in range(1, n + 1)]
    for i in range(2, len(a)):
        a[i], a[i // 2] = a[i // 2], a[i]
    return a


if __name__ == '__main__':
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    n = read_lines(path_input)[0][0]
    worst_array = task2(n)

    write_in_file(path_output, worst_array)
    print(worst_array)
