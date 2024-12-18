from lab4.utils import read_data, write_data


def format_data(commands: list) -> list:
    """
    Форматирует данные под задачу

    Пример:
    ['+ 1', '?', '-', '+ 13'] -> ['1', '?', '-', '13']
    """
    commands_format = []
    for i in commands:
        i_split = i.split()
        if len(i_split) == 2:
            commands_format.append(i_split[1])
        else:
            commands_format.append(i_split[0])
    return commands_format


def get_queue_minimals(commands: list) -> list:
    """
    Получает минимальные элементы из очереди по ходу выполнения команд

    Пример:
    ['1', '?', '-', '13', '4', '?'] -> ['1', '4']
    """
    queue = []
    minimals = []
    for i in commands:
        if i == '?':
            min_element = str(min([int(i) for i in queue]))
            minimals.append(min_element)
        elif i == '-':
            queue.pop(0)
        else:
            queue.append(i)
    return minimals


def task6():
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    commands = read_data(PATH_INPUT)[1:]  # не считаем первую строчку, так как там количество элементов
    commands_format = format_data(commands)

    result = get_queue_minimals(commands_format)
    result_format = '\n'.join(result)

    write_data(PATH_OUTPUT, result_format)
    print(result_format)


if __name__ == "__main__":
    task6()
