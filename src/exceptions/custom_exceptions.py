"""
Custom exceptions for the PDF Document Analyzer application.
"""
class PDFAnalyzerException(Exception):
    """
    Base exception for all application-specific exceptions.
    """

    pass


class InvalidPDFException(PDFAnalyzerException):
    """
    Raised when the uploaded file is not a valid PDF.
    """

    pass


class FileStorageException(PDFAnalyzerException):
    """
    Raised when the uploaded file cannot be saved.
    """

    pass


class PDFExtractionException(PDFAnalyzerException):
    """
    Raised when text extraction from a PDF fails.
    """

    pass


class KeywordSearchException(PDFAnalyzerException):
    """
    Raised when keyword search fails.
    """

    pass