from lab2.utils import write_in_file, write_info, start_collect


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])

    i, j = 0, 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
    return A


def main(input_file, output_file, info_file):
    t_start, tracemalloc, in_f = start_collect(input_file)

    A = [int(x) for x in in_f[1].split()]
    p, r = 0, len(A) - 1
    A = MergeSort(A, p, r)
    res_s = ''
    for i in A:
        res_s += str(i) + ' '

    write_info(info_file, t_start, tracemalloc)
    write_in_file(output_file, res_s)
