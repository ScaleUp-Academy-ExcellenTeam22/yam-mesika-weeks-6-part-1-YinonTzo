

def words_length(sentence: str) -> dict[str: int]:
    """
    :param sentence: Some string to split.
    :return: Dict which contains every word and its length.
    """
    return {word: len(word) for word in sentence.split(" ")}


if __name__ == '__main__':
    lengths = words_length("Yinon Tzomi 25 years old")
    print(lengths)

    lengths = words_length("Toto, I've a feeling we're not in Kansas anymore")
    print(lengths)
