from src.logging import logger

def count_keyword_occurrences(text, keyword):
    """ Count how many times a keyword appears in text. """
    logger.info("Searching keyword: %s", keyword)

    logger.info(
        "Keyword '%s' found %d times.",
        keyword,
        text.lower().count(
            keyword.lower()
            )
    )
    # Ignore upper/lower case differences
    return text.lower().count(
        keyword.lower()
    )