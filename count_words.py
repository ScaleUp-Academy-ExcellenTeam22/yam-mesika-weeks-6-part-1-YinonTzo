import string


def clean_text(text: str) -> list:
    """
    https://towardsdatascience.com/how-to-efficiently-remove-punctuations-from-a-string-899ad4a059fb
    Makes table which include all signs to remove. Then translate the text and split it.
    :param text: Text with punctuations, whitespaces and numbers
    :return: List with only words
    """
    exclist = string.punctuation + string.digits
    table = str.maketrans('', '', exclist)
    return text.translate(table).split()


def words_length(sentence: list) -> dict[str: int]:
    """
    :param sentence: Some string to split.
    :return: Dict which contains every word and its length.
    """
    return {word: len(word) for word in sentence}


if __name__ == '__main__':
    text_to_parse = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    new_text = words_length(clean_text(text_to_parse))
    print(new_text)
