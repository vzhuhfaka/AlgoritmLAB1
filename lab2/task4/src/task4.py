from lab2.utils import read_lines, write_in_file


def BinSearch(A, n):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        if A[0] == n:
            return 0
        return -1

    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if n == A[mid]:
            return mid
        elif n > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def task4():
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    # Берём вторую строчку, так как в первой число элементов к списку чисел
    array = read_lines(path_input)[1]

    # берём четвертую строчку, так как в третьей число элементов к списку чисел, которые нужно найти
    to_search_n = read_lines(path_input)[3]
    result = ''

    for i in to_search_n:
        result += str(BinSearch(array, i)) + ' '

    write_in_file(path_output, result)
    print(result)


if __name__ == '__main__':
    task4()