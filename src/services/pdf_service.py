import os

from pypdf import PdfReader

from src.exceptions import PDFExtractionException
from src.logging import logger


def extract_text_from_pdf(
    file_path: str
) -> str:
    """
    Extract text from every page of a PDF document.

    Parameters
    ----------
    file_path : str
        Absolute path of the PDF document.

    Returns
    -------
    str
        Extracted text from the PDF.

    Raises
    ------
    PDFExtractionException
        Raised when text extraction fails.
    """

    try:

        # ==========================================================
        # Open PDF Document
        # ==========================================================

        logger.info(
            "Starting PDF text extraction."
        )

        reader = PdfReader(file_path)

        # ==========================================================
        # Extract Text From All Pages
        # ==========================================================

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        # ==========================================================
        # Return Extracted Text
        # ==========================================================

        logger.info(
            "PDF text extraction completed."
        )

        return text

    except Exception as ex:

        logger.error(
            "PDF extraction failed.",
            exc_info=True
        )

        raise PDFExtractionException(
            "Unable to extract text from the uploaded PDF."
        ) from ex


def get_pdf_metadata(
    file_path: str
) -> dict:
    """
    Retrieve metadata from a PDF document.

    Parameters
    ----------
    file_path : str
        Absolute path of the PDF document.

    Returns
    -------
    dict
        Dictionary containing page count and file size.

    Raises
    ------
    PDFExtractionException
        Raised when metadata extraction fails.
    """

    try:

        # ==========================================================
        # Open PDF Document
        # ==========================================================

        logger.info(
            "Reading PDF metadata."
        )

        reader = PdfReader(file_path)

        # ==========================================================
        # Read PDF Metadata
        # ==========================================================

        page_count = len(reader.pages)

        file_size_mb = round(
            os.path.getsize(file_path) / (1024 * 1024),
            2
        )

        # ==========================================================
        # Return Metadata
        # ==========================================================

        logger.info(
            "PDF metadata generated successfully."
        )

        return {
            "page_count": page_count,
            "file_size_mb": file_size_mb
        }

    except Exception as ex:

        logger.error(
            "PDF metadata extraction failed.",
            exc_info=True
        )

        raise PDFExtractionException(
            "Unable to read PDF metadata."
        ) from ex