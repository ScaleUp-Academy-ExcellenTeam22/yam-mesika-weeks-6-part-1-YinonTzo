import time


def timer(function: callable, *args, **kwargs):
    """
    :param function: Function to run.
    :param args: Arguments for function.
    :param kwargs: Arguments for function.
    :return: How long it took to function to run
    """
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
