# PDF Document Analyzer

A Python-based desktop application for extracting and analyzing text from PDF documents.

## Features

* Select PDF files through a GUI
* Extract text from PDF documents
* Search keywords in extracted text
* Display keyword occurrence count
* Validate PDF file size
* Export extracted text to a file
* User-friendly Tkinter interface

## Technologies Used

* Python 3
* Tkinter
* PyPDF
* Git & GitHub

## Project Structure

PDFDocumentAnalyzer/

├── src/

│ ├── ui/

│ ├── services/

│ └── utils/

├── data/

│ ├── input/

│ └── output/

├── .gitignore

├── README.md

└── requirements.txt

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python -m src.ui.pdf_document_analyzer
```

## Current Features

* PDF Text Extraction
* Keyword Search
* Text Export
* File Size Validation
* Refactored Project Structure

## Future Enhancements

* Keyword Highlighting
* PDF Metadata Extraction
* Export to DOCX
* Search History
* Dark Mode UI

## Git Workflow

main → develop → feature/*

## Author

Avneesh Srivastava
