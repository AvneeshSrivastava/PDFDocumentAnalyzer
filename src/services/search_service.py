from src.exceptions import KeywordSearchException
from src.logging import logger


def count_keyword_occurrences(
    text: str,
    keyword: str
) -> int:
    """
    Count the number of occurrences of a keyword in the given text.

    Parameters
    ----------
    text : str
        Text to search.

    keyword : str
        Keyword to search.

    Returns
    -------
    int
        Total number of matches.

    Raises
    ------
    KeywordSearchException
        Raised when keyword search fails.
    """

    try:

        # ==========================================================
        # Perform Case-Insensitive Search
        # ==========================================================

        logger.info(
            "Searching keyword: %s",
            keyword
        )

        count = text.lower().count(
            keyword.lower()
        )

        logger.info(
            "Keyword '%s' found %d times.",
            keyword,
            count
        )

        return count

    except Exception as ex:

        logger.error(
            "Keyword search failed.",
            exc_info=True
        )

        raise KeywordSearchException(
            "Unable to search the keyword."
        ) from ex