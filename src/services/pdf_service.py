from pypdf import PdfReader
import os


def extract_text_from_pdf(file_path):
    """
    Extract all text from a PDF file.
    """

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

    return text

def get_pdf_metadata(file_path):
    """
    Get basic PDF information such as:
    - Number of pages
    - File size in MB
    """

    # Open the PDF file
    reader = PdfReader(file_path)

    # Count total pages in the PDF
    page_count = len(reader.pages)

    # Get file size in MB
    file_size_mb = round(
        os.path.getsize(file_path) / (1024 * 1024),
        2
    )

    # Return metadata as a dictionary
    return {
        "page_count": page_count,
        "file_size_mb": file_size_mb
    }