from fastapi import Form
from src.services.search_service import count_keyword_occurrences
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from src.logging import logger
from src.services.file_service import save_uploaded_file
from src.services.pdf_service import (
    extract_text_from_pdf,
    get_pdf_metadata
)

import re
from src.config import settings
from src.validators import validate_pdf
from src.exceptions.custom_exceptions import PDFAnalyzerException


# Temporary storage for extracted text
pdf_text = ""
router = APIRouter()

templates = Jinja2Templates(
    directory=settings.TEMPLATE_FOLDER
)

@router.get("/")
def home(reqest:Request):

    return templates.TemplateResponse(
        request=reqest,
        name="index.html"
    )

@router.get("/upload")
def search_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": "Please upload a valid PDF.",
            "show_sidebar": True
        },
        status_code=400
    )
@router.post("/upload")
async def upload_pdf(
    request: Request,
    pdf_file: UploadFile = File(...)
):
    logger.info("PDF upload request received.")
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

    # Store extracted text for keyword search
    pdf_text = extracted_text

    # Get PDF metadata such as page count and file size
    metadata = get_pdf_metadata(
    file_path
    )
    logger.info("Returning extraction result page.")
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "extracted_text": extracted_text,
            "metadata": metadata
        }
    )

@router.get("/search")
def search_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": "Please upload a PDF before searching.",
            "show_sidebar": True
        },
        status_code=400
    )

@router.post("/search")
def search_keyword(request: Request, keyword: str = Form(...)):

    logger.info("Search Started.")
    if not pdf_text:
        raise PDFAnalyzerException(
            "No PDF document is available. Please upload a PDF before searching."
        )
    count = count_keyword_occurrences(pdf_text, keyword)

    highlighted_text = highlight_text(pdf_text, keyword)

    logger.info("Search completed.")
    return templates.TemplateResponse(
        request=request,
        name="search_result.html",
        context={
            "keyword": keyword,
            "count": count,
            "highlighted_text": highlighted_text
        }
    )

def highlight_text(text: str, keyword: str):
    logger.info("Text highliting Started.")
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    logger.info("Text highliting Completed.")
    return pattern.sub(r"<mark>\g<0></mark>", text)