def read_numbers() -> map:
    """
    Read numbers from standard input.
    The input must be separated with ','. for example: 10,-7,6,5
    :return: Map with all numbers as int
    """
    return map(int, input().split(','))


def positive_numbers(numbers: map) -> list:
    """
    Filter all negative numbers.
    :param numbers: map of numbers.
    :return: List with all values are positive
    """
    return list(filter(lambda num: num >= 0, numbers))


def main() -> None:
    """
    Read numbers from user and print only the positives.
    """
    numbers = read_numbers()
    print(positive_numbers(numbers))


if __name__ == '__main__':
    main()
