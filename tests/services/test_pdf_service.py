from unittest.mock import MagicMock, patch

import pytest


from src.exceptions import PDFExtractionException
from src.services.pdf_service import extract_text_from_pdf, get_pdf_metadata

@patch("src.services.pdf_service.PdfReader")
def test_extract_text_from_pdf_success(mock_pdf_reader):

    mock_page_1 = MagicMock()
    mock_page_1.extract_text.return_value = "Hello "

    mock_page_2 = MagicMock()
    mock_page_2.extract_text.return_value = "World"

    mock_reader = MagicMock()
    mock_reader.pages = [
        mock_page_1,
        mock_page_2
    ]

    mock_pdf_reader.return_value = mock_reader

    result = extract_text_from_pdf(
        "dummy.pdf"
    )

    assert result == "Hello World"

@patch("src.services.pdf_service.PdfReader")
def test_extract_text_from_pdf_failure(mock_pdf_reader):

    mock_pdf_reader.side_effect = Exception(
        "Unable to read PDF"
    )

    with pytest.raises(
        PDFExtractionException
    ):

        extract_text_from_pdf(
            "dummy.pdf"
        )

@patch("src.services.pdf_service.os.path.getsize")
@patch("src.services.pdf_service.PdfReader")
def test_get_pdf_metadata_success(
    mock_pdf_reader,
    mock_getsize
):

    mock_reader = MagicMock()
    mock_reader.pages = [MagicMock(), MagicMock(), MagicMock()]

    mock_pdf_reader.return_value = mock_reader

    mock_getsize.return_value = 2 * 1024 * 1024

    result = get_pdf_metadata("dummy.pdf")

    assert result == {
    "page_count": 3,
    "file_size_mb": 2
    }

@patch("src.services.pdf_service.PdfReader")
def test_get_pdf_metadata_failure(
    mock_pdf_reader
):

    mock_pdf_reader.side_effect = Exception(
        "Metadata Error"
    )

    with pytest.raises(
        PDFExtractionException
    ):

        get_pdf_metadata("dummy.pdf")