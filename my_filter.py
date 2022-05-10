from typing import Callable, Iterable, Generator


def my_filter(function: Callable, iterable: Iterable) -> Generator:
    """
    Implement filter function.
    :param function: Bool function
    :param iterable: Some iterable to pass over
    :return: Generator which holds all values are return True to function
    """
    for item in iterable:
        if function(item):
            yield item


if __name__ == '__main__':
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = filter(lambda age: age >= 18, ages)
    mature_ages_my_filter = my_filter(lambda age: age >= 18, ages)
    print(tuple(mature_ages))
    print(tuple(mature_ages_my_filter))
