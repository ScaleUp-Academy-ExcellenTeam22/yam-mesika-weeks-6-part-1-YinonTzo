def get_letters() -> tuple:
    """
    :return: List of lowercase and list of uppercase letters.
    """
    return (create_list_letters('a', 'z'),
            create_list_letters('A', 'Z'))


def create_list_letters(start: chr, end: chr) -> list:
    """
    Makes range of int- using ord function between start to end.
    Then, maps all range to chr and returns it.
    :param start: Start range.
    :param end: End range.
    :return: List of letters between start to end.
    """
    return [chr(letter) for letter in range(ord(start), ord(end) + 1)]


if __name__ == '__main__':
    print(get_letters())
