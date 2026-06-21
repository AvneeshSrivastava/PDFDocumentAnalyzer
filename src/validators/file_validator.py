import os

from fastapi import UploadFile

from src.config import settings
from src.exceptions import InvalidPDFException


def validate_pdf(
    uploaded_file: UploadFile,
    content: bytes
):
    """
    Validate an uploaded PDF file.

    This function performs multiple validation checks before the
    file is processed by the application.

    Validation Steps
    ----------------
    1. Verify a file has been selected.
    2. Validate the file extension.
    3. Validate the MIME content type.
    4. Ensure the uploaded file is not empty.
    5. Verify the file size does not exceed the configured limit.

    Parameters
    ----------
    uploaded_file : UploadFile
        Uploaded file received from the client.

    content : bytes
        Binary content of the uploaded file.

    Raises
    ------
    InvalidPDFException
        Raised when any validation rule fails.
    """

    # ==========================================================
    # Validate File Name
    # ==========================================================

    # Ensure that the user selected a file.
    if not uploaded_file.filename:
        raise InvalidPDFException(
            "No file was selected."
        )

    # ==========================================================
    # Validate File Extension
    # ==========================================================

    # Extract the uploaded file extension.
    _, extension = os.path.splitext(
        uploaded_file.filename
    )

    # Normalize the extension for comparison.
    extension = extension.lower()

    # Ensure the uploaded file has a supported extension.
    if extension not in settings.ALLOWED_FILE_EXTENSIONS:
        raise InvalidPDFException(
            "Only PDF files are allowed."
        )

    # ==========================================================
    # Validate MIME Type
    # ==========================================================

    # Verify the uploaded content type.
    if uploaded_file.content_type not in settings.ALLOWED_CONTENT_TYPES:
        raise InvalidPDFException(
            "Invalid file type. Please upload a valid PDF document."
        )

    # ==========================================================
    # Validate Empty File
    # ==========================================================

    # Ensure the uploaded file contains data.
    if not content:
        raise InvalidPDFException(
            "The uploaded file is empty."
        )

    # ==========================================================
    # Validate Maximum File Size
    # ==========================================================

    # Convert configured file size limit (MB) to bytes.
    max_size_bytes = settings.MAX_FILE_SIZE_MB * 1024 * 1024

    # Verify that the uploaded file does not exceed
    # the configured maximum size.
    if len(content) > max_size_bytes:
        raise InvalidPDFException(
            f"Maximum allowed file size is "
            f"{settings.MAX_FILE_SIZE_MB} MB."
        )