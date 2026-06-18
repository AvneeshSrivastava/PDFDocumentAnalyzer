from pypdf import PdfReader
import os
from src.logging import logger
from src.exceptions.custom_exceptions import PDFExtractionException


def extract_text_from_pdf(file_path):
    """
    Extract all text from a PDF file.
    """
    try:
        logger.info("Starting PDF text extraction.")
        # Open the PDF file
        reader = PdfReader(file_path)

        # Store extracted text from all pages
        text = ""

        # Loop through every page in the PDF
        for page in reader.pages:

            # Extract text from current page
            extracted = page.extract_text()

            # Add text only if extraction was successful
            if extracted:
                text += extracted

        logger.info("PDF text extraction completed.")
        return text
    except Exception as ex:
        logger.error(
            "PDF extraction failed.",
            exc_info=True
        )

        raise PDFExtractionException(
            "Unable to extract text from the uploaded PDF."
        ) from ex

def get_pdf_metadata(file_path):
    """
    Get basic PDF information such as:
    - Number of pages
    - File size in MB
    """
    try:

        logger.info("Reading PDF metadata.")
        # Open the PDF file
        reader = PdfReader(file_path)

        # Count total pages in the PDF
        page_count = len(reader.pages)

        # Get file size in MB
        file_size_mb = round(
            os.path.getsize(file_path) / (1024 * 1024),
            2
        )
        logger.info("PDF metadata generated successfully.")
        # Return metadata as a dictionary
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