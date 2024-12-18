
def read_data(path: str) -> list:
    with open(path, 'r') as f:
        return [i.strip() for i in f.readlines()]


def write_data(path: str, text: str) -> None:
    with open(path, 'w') as f:
        f.write(text)

__all__ = ['read_data', 'write_data']