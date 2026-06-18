import os

from fastapi import UploadFile

from src.config import settings
from src.exceptions import InvalidPDFException


def validate_pdf(uploaded_file: UploadFile,content:bytes):
    """
    Validate the uploaded PDF file.
    """

    # Ensure filename exists
    if not uploaded_file.filename:
        raise InvalidPDFException(
            "No file was selected."
        )

    # Get file extension
    _, extension = os.path.splitext(
        uploaded_file.filename
    )

    # Convert extension to lowercase
    extension = extension.lower()

    # Validate file extension
    if extension not in settings.ALLOWED_FILE_EXTENSIONS:
        raise InvalidPDFException(
            "Only PDF files are allowed."
        )
    # Validate empty file
    if not content:
        raise InvalidPDFException(
            "The uploaded file is empty."
        )

    # Validate maximum file size
    max_size_bytes = settings.MAX_FILE_SIZE_MB * 1024 * 1024

    if len(content) > max_size_bytes:
        raise InvalidPDFException(
            f"Maximum allowed file size is "
            f"{settings.MAX_FILE_SIZE_MB} MB."
        )