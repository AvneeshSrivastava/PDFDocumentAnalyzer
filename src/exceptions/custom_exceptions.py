"""
Custom exception classes for the PDF Document Analyzer application.

This module defines all application-specific exceptions used throughout
the project. Having custom exceptions provides the following benefits:

1. Improves code readability.
2. Enables centralized exception handling.
3. Makes debugging easier.
4. Separates application errors from built-in Python exceptions.
5. Allows meaningful error messages to be displayed to users.
"""


class PDFAnalyzerException(Exception):
    """
    Base exception for the PDF Document Analyzer application.

    All custom exceptions should inherit from this class so they can
    be handled by a single global exception handler.
    """

    pass


class InvalidPDFException(PDFAnalyzerException):
    """
    Raised when an uploaded file is not a valid PDF.

    Example scenarios:
    - Unsupported file extension.
    - Invalid MIME type.
    - Corrupted PDF document.
    - Empty PDF file.
    """

    pass


class FileStorageException(PDFAnalyzerException):
    """
    Raised when an uploaded PDF cannot be stored successfully.

    Example scenarios:
    - Permission denied.
    - Disk write failure.
    - Invalid destination path.
    - Storage device unavailable.
    """

    pass


class PDFExtractionException(PDFAnalyzerException):
    """
    Raised when text extraction from a PDF document fails.

    Example scenarios:
    - Encrypted PDF.
    - Corrupted PDF.
    - Unsupported PDF structure.
    - PDF processing library error.
    """

    pass


class KeywordSearchException(PDFAnalyzerException):
    """
    Raised when keyword searching cannot be completed.

    Example scenarios:
    - Search text is unavailable.
    - Invalid search keyword.
    - Regular expression failure.
    - Unexpected search processing error.
    """
    pass