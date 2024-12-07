from lab2.utils import read_lines, write_in_file


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] + right[j:]
    return res


def merge_sort(A):
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    array = read_lines(path_input)[1]  # берём вторую строчку, так как в первой число элементов
    sorted_array = merge_sort(array)

    write_in_file(path_output, array)
    print(sorted_array)
