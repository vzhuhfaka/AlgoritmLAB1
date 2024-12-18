from lab4.utils import read_data, write_data


def check_brackets(brackets_: str) -> bool:
    """
    Проверяет правильность скобочных последовательностей

    Пример: '()[[))' -> False
            '()[()]' -> True
    """
    stack = []
    matching_brackets = {')': '(', ']': '['}
    for i in brackets_:
        if i in '([':
            stack.append(i)  # добавляем в стек скобку, которая ещё не закрыта
        else:
            # Проверяем в стеке наличие скобки, которая закрывает текущую
            if not stack or stack[-1] != matching_brackets[i]:
                return False
            stack.pop()

    return not stack


def task3():
    PATH_INPUT = '../txtf/input.txt'
    PATH_OUTPUT = '../txtf/output.txt'

    brackets = read_data(PATH_INPUT)
    answer = ''
    for i in brackets[1:]:
        if check_brackets(i):
            answer += 'YES\n'
        else:
            answer += 'NO\n'

    write_data(PATH_OUTPUT, answer)
    print(answer)


if __name__ == "__main__":
    task3()
