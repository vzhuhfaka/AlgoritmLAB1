def read_lines(file):
    lines = []
    with open(file, 'r') as f:
        for i in f.readlines():
            el = []
            for j in i.strip().split():
                el.append(j)
            lines.append(el)
    return lines

def write_in_file(file, text):
    with open(file, 'w+') as f:
        if isinstance(text, list):
            f.write(str(text)[1:-1])
        elif isinstance(text, str):
            f.write(text)
