from src.logging import logger
from src.exceptions.custom_exceptions import KeywordSearchException

def count_keyword_occurrences(text, keyword):
    """ Count how many times a keyword appears in text. """
    try:
        logger.info("Searching keyword: %s", keyword)
        normalized_text = text.lower()
        normalized_keyword = keyword.lower()
        count = normalized_text.count(
            normalized_keyword
        )
        logger.info(
            "Keyword '%s' found %d times.",
            keyword,
            count
        )
        # Ignore upper/lower case differences
        return count
    except Exception as ex:
        logger.error(
            "Keyword search failed.",
            exc_info=True
        )

        raise KeywordSearchException(
            "Unable to search the keyword."
        ) from ex