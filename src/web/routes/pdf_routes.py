import re

from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates

from src.config import settings
from src.exceptions import PDFAnalyzerException
from src.logging import logger
from src.services.file_service import save_uploaded_file
from src.services.pdf_service import (
    extract_text_from_pdf,
    get_pdf_metadata
)
from src.services.search_service import count_keyword_occurrences
from src.validators import validate_pdf

# ==========================================================
# Global Variables
# ==========================================================

# Temporarily stores extracted PDF text for keyword searching.
pdf_text: str = ""

router = APIRouter()

templates = Jinja2Templates(
    directory=settings.TEMPLATE_FOLDER
)


# ==========================================================
# Home Page
# ==========================================================

@router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================================================
# Handle Direct Access to Upload Endpoint
# ==========================================================

@router.get("/upload")
def upload_page_error(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": "Please upload a valid PDF.",
            "show_sidebar": True
        },
        status_code=400
    )


# ==========================================================
# Upload PDF
# ==========================================================

@router.post("/upload")
async def upload_pdf(
    request: Request,
    pdf_file: UploadFile = File(...)
):

    logger.info(
        "PDF upload request received."
    )

    content = await pdf_file.read()

    validate_pdf(
        uploaded_file=pdf_file,
        content=content
    )

    global pdf_text

    file_path = save_uploaded_file(
        pdf_file.filename,
        content
    )

    extracted_text = extract_text_from_pdf(
        file_path
    )

    pdf_text = extracted_text

    metadata = get_pdf_metadata(
        file_path
    )

    logger.info(
        "Returning extraction result page."
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "extracted_text": extracted_text,
            "metadata": metadata
        }
    )


# ==========================================================
# Handle Direct Access to Search Endpoint
# ==========================================================

@router.get("/search")
def search_error_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": "Please upload a PDF before searching.",
            "show_sidebar": True
        },
        status_code=400
    )


# ==========================================================
# Search Keyword
# ==========================================================

@router.post("/search")
def search_keyword(
    request: Request,
    keyword: str = Form(...)
):

    logger.info(
        "Keyword search started."
    )

    if not pdf_text:
        raise PDFAnalyzerException(
            "No PDF document is available. Please upload a PDF before searching."
        )

    count = count_keyword_occurrences(
        pdf_text,
        keyword
    )

    highlighted_text = highlight_text(
        pdf_text,
        keyword
    )

    logger.info(
        "Keyword search completed."
    )

    return templates.TemplateResponse(
        request=request,
        name="search_result.html",
        context={
            "keyword": keyword,
            "count": count,
            "highlighted_text": highlighted_text
        }
    )


# ==========================================================
# Highlight Search Results
# ==========================================================

def highlight_text(
    text: str,
    keyword: str
) -> str:
    """
    Highlight all occurrences of a keyword in the extracted text.
    """

    logger.info(
        "Text highlighting started."
    )

    pattern = re.compile(
        re.escape(keyword),
        re.IGNORECASE
    )

    logger.info(
        "Text highlighting completed."
    )

    return pattern.sub(
        r"<mark>\g<0></mark>",
        text
    )