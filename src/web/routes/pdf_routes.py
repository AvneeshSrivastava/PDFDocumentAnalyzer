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

@router.post("/upload")
async def upload_pdf(
    request: Request,
    pdf_file: UploadFile = File(...)
):
    logger.info("PDF upload request received.")
    global pdf_text
    content = await pdf_file.read()

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

@router.post("/search")
def search_keyword(request: Request, keyword: str = Form(...)):

    logger.info("Search Started.")
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