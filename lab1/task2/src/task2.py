from lab1.utils import read_lines, write_in_file


def linearfinder(ar, n):
    res_n = []
    for i in range(len(ar)):
        if ar[i] == n:
            res_n.append(i)
    return res_n


def task2():
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array = read_lines(path_input)[0]
    need_to_find = read_lines(path_input)[1][0]
    found_n = linearfinder(array, need_to_find)

    write_in_file(path_output, found_n)
    print(found_n)


if __name__ == '__main__':
    task2()