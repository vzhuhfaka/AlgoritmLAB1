from lab2.utils import read_lines, write_in_file


def majority_number(A):
    if len(A) == 1:
        return A[0]

    q = len(A) // 2
    left = majority_number(A[:q])
    right = majority_number(A[q:])

    if left == right:
        return left

    left_count = A.count(left)
    right_count = A.count(right)

    if left_count > right_count:
        return left
    else:
        return right


def majority(array):
    if array.count(majority_number(array)) > len(array) / 2:
        return 1
    else:
        return 0


def task5():
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    # Берём вторую строчку, так как в первой число элементов к списку чисел
    array = read_lines(path_input)[1]

    result = majority(array)

    write_in_file(path_output, result)
    print(result)


if __name__ == '__main__':
    task5()
