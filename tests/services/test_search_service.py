import pytest


from src.exceptions import KeywordSearchException
from src.services.search_service import count_keyword_occurrences


def test_count_keyword_occurrences_single_match():

    text = "Python is awesome"
    result = count_keyword_occurrences(
        text,
        "Python"
    )
    assert result == 1

def test_count_keyword_occurrences_multiple_matches():

    text = "Python Python Python"

    result = count_keyword_occurrences(
        text,
        "Python"
    )

    assert result == 3

def test_count_keyword_occurrences_case_insensitive():

    text = "Python python PYTHON"

    result = count_keyword_occurrences(
        text,
        "python"
    )

    assert result == 3

def test_count_keyword_occurrences_not_found():

    text = "Java C++"

    result = count_keyword_occurrences(
        text,
        "Python"
    )

    assert result == 0
def test_count_keyword_occurrences_empty_text():

    result = count_keyword_occurrences(
        "",
        "Python"
    )

    assert result == 0

def test_count_keyword_occurrences_exception():

    with pytest.raises(
        KeywordSearchException
    ):

        count_keyword_occurrences(
            None,
            "Python"
        )