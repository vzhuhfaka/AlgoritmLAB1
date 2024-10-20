import time, tracemalloc


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])

    L.append(float('inf'))
    R.append(float('inf'))

    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
    return A

def main(input_file, output_file, info_file):
    t_start = time.perf_counter()
    tracemalloc.start()

    in_f = open(input_file, 'r').readlines()
    out_f = open(output_file, 'w+')
    info_f = open(info_file, 'w+')

    n = in_f[0].strip()
    A = [int(x) for x in in_f[1].split()]

    p, r = 0, len(A) - 1

    A = MergeSort(A, p, r)

    info_f.write(f'time: {time.perf_counter() - t_start} s\nmemory: {tracemalloc.get_traced_memory()[1] / 2 ** 20} Mb')
    tracemalloc.stop()

    res_s = ''
    for i in A:
        res_s += str(i) + ' '

    out_f.write(res_s)