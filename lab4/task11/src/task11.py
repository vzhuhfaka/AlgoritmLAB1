from lab4.utils import read_data, write_data


def get_rest(data, certificates):
    """
    Решает задачу

    Пример: get_rest([1, 2, 3], 5) -> [3, [4, 1, 2]]
    """
    c = 0  # индекс человека в очереди
    for i in range(int(certificates)):
        if not data:  # если закончились люди в очереди
            return -1

        c = c % len(data)  # сбрасываем этот индекс, так как очередь закончилась
        data[c] = int(data[c]) - 1
        if data[c] == 0:
            data.pop(c)
        c += 1

    return [len(data), data]


def task11():
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    # В первой строке берём второе значение, так как это количество выдаваемых справок
    certificates_number = read_data(PATH_INPUT)[0].split()[1]
    queue = read_data(PATH_INPUT)[1].split()

    result = get_rest(queue, certificates_number)

    if result == -1:
        write_data(PATH_OUTPUT, str(result))
    else:
        write_data(PATH_OUTPUT, f'{result[0]} \n{str(result[1])[1:-1]}')
    print(result[1])


if __name__ == "__main__":
    task11()
