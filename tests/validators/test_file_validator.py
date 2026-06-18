from io import BytesIO
from fastapi import UploadFile
from src.validators import validate_pdf
import pytest

from src.exceptions import InvalidPDFException

def test_validate_pdf_with_valid_pdf():

    file = UploadFile(
        filename="resume.pdf",
        file=BytesIO(b"Dummy PDF Content")
    )

    content = b"Dummy PDF Content"

    # Should not raise any exception
    validate_pdf(
        uploaded_file=file,
        content=content
    )

def test_validate_pdf_with_invalid_extension():

    file = UploadFile(
        filename="resume.txt",
        file=BytesIO(b"Dummy Content")
    )

    content = b"Dummy Content"

    with pytest.raises(InvalidPDFException):

        validate_pdf(
            uploaded_file=file,
            content=content
        )

def test_validate_pdf_with_empty_file():

    file = UploadFile(
        filename="resume.pdf",
        file=BytesIO(b"")
    )

    content = b""

    with pytest.raises(InvalidPDFException):

        validate_pdf(
            uploaded_file=file,
            content=content
        )

def test_validate_pdf_with_large_file():

    file = UploadFile(
        filename="resume.pdf",
        file=BytesIO(b"")
    )

    large_content = b"x" * (
    (11 * 1024 * 1024)
    )

    with pytest.raises(InvalidPDFException):

        validate_pdf(
            uploaded_file=file,
            content=large_content
        )