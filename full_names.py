def full_names(first_names: list, last_names: list, min_length: int = None) -> list:
    """
    :param first_names: List that contain first names.
    :param last_names: List that contain last names.
    :param min_length: Optional parameter that contain the min length of full name.
    :return: List that contain full name.
    """
    full_names_list = [first_name.title() + " " + last_name.title()
                       for first_name in first_names
                       for last_name in last_names]

    if not min_length:
        return full_names_list

    return list(filter(lambda name: len(name) >= min_length, full_names_list))


def main():
    """
    Main function
    """
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))


if __name__ == '__main__':
    main()
