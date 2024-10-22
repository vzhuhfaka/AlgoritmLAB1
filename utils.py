def close_files(*args):
    for i in args:
        i.close()


def write_info(file, _time, memory):
    with open(file, 'w+') as f:
        f.write(f'time: {_time} s\nmemory: {memory} Mb')


def list_to_str(ar):
    res = ''
    for i in ar:
        res += str(i)
    return str(int(res))


def str_to_list(s):
    s = str(s)
    res = []
    for i in s:
        res.append(i)
    return res


def read_file(file):
    with open(file, 'r') as f:
        return f.readlines()


def write_file(file, text):
    with open(file, 'w+') as f:
        f.write(text)


def txt_to_str(file_txt):
    with open(file_txt, 'r') as f:
        return f.readline()


def txt_to_numlist(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline():
            if i in '0123456789':
                res.append(i)
    return res


def txt_to_list(file_txt):
    res = []
    with open(file_txt, 'r') as f:
        for i in f.readline().split():
            res.append(int(i))
    return res