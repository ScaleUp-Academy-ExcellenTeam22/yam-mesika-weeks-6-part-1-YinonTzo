def read_numbers() -> map:
    """
    Reads numbers from standard input.
    :return: Map with all numbers as int
    """
    return map(int, input().split(','))


def positive_numbers() -> list:
    """
    :return: List with all values are positive
    """
    numbers = read_numbers()
    return list(filter(lambda num: num >= 0, numbers))


if __name__ == '__main__':
    print(positive_numbers())
