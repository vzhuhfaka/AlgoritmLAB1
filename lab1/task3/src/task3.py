from lab1.utils import read_lines, write_in_file


def bin_sum(A, B):
    C = ""
    t = 0
    A = A[::-1]
    B = B[::-1]

    for i in range(len(A)):
        a = int(A[i])
        b = int(B[i])
        c = a + b + t
        C = str(c % 2) + C
        t = c // 2

    if t > 0:
        C = str(t) + C

    return C


def task3():
    path_input = '../txtf/input.txt'
    path_output = '../txtf/output.txt'

    input_str = read_lines(path_input)[0]
    A = input_str[0]
    B = input_str[1]
    C = bin_sum(A, B)

    write_in_file(path_output, C)
    print(C)


if __name__ == '__main__':
    task3()
