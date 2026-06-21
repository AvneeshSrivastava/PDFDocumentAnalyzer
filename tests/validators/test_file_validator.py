from io import BytesIO
import pytest
from fastapi import UploadFile
from starlette.datastructures import Headers

from src.exceptions import InvalidPDFException
from src.validators import validate_pdf

def test_validate_pdf_with_valid_pdf():

    file = UploadFile(
        filename="resume.pdf",
        file=BytesIO(b"Dummy PDF Content"),
        headers=Headers({
            "content-type": "application/pdf"
        })
    )

    content = b"Dummy PDF Content"

    validate_pdf(
        uploaded_file=file,
        content=content
    )

def test_validate_pdf_with_invalid_extension():

    file = UploadFile(
        filename="resume.txt",
        file=BytesIO(b"Dummy Content"),
        headers=Headers({
            "content-type": "application/pdf"
        })
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
        file=BytesIO(b""),
        headers=Headers({
            "content-type": "application/pdf"
        })
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
        file=BytesIO(b""),
        headers=Headers({
            "content-type": "application/pdf"
        })
    )

    large_content = b"x" * (11 * 1024 * 1024)

    with pytest.raises(InvalidPDFException):

        validate_pdf(
            uploaded_file=file,
            content=large_content
        )