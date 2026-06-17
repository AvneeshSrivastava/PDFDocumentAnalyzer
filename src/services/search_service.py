def count_keyword_occurrences(text, keyword):
    """ Count how many times a keyword appears in text. """

    # Ignore upper/lower case differences
    return text.lower().count(
        keyword.lower()
    )