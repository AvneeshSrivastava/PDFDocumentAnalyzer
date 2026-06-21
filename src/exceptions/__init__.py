"""
__init__.py

This file initializes the PDF Analyzer package.

- Purpose:
  Expose commonly used custom exceptions at the package level
  so they can be imported directly from `pdf_analyzer` instead
  of digging into submodules.

- Usage:
  from pdf_analyzer import PDFAnalyzerException, InvalidPDFException

- Notes:
"""

from .custom_exceptions import (
    PDFAnalyzerException as PDFAnalyzerException,
    InvalidPDFException as InvalidPDFException,
    FileStorageException as FileStorageException,
    PDFExtractionException as PDFExtractionException,
    KeywordSearchException as KeywordSearchException,
)