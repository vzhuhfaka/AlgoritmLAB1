from lab1.utils import read_lines, write_in_file


def insertionsort(ar):
    for i in range(1, len(ar)):
        value = ar[i]
        j = i - 1
        while value < ar[j] and j >= 0:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = value
    return ar


def task1():
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array = read_lines(path_input)[1]  # берём вторую строчку, так как в первой число элементов
    sorted_array = insertionsort(array)

    write_in_file(path_output, sorted_array)
    print(sorted_array)


if __name__ == '__main__':
    task1()