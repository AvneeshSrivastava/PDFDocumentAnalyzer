from fastapi import Form
from src.services.search_service import count_keyword_occurrences
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates

from src.services.file_service import save_uploaded_file
from src.services.pdf_service import (
    extract_text_from_pdf,
    get_pdf_metadata
)

# Temporary storage for extracted text
pdf_text = ""
router = APIRouter()

templates = Jinja2Templates(directory="templates")

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

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "extracted_text": extracted_text,
            "metadata": metadata
        }
    )

@router.post("/search")
def search_keyword(request:Request, keyword : str = Form(...)):
    count = count_keyword_occurrences(
        pdf_text,
        keyword
    )

    return templates.TemplateResponse(
        request=request,
        name="search_result.html",
        context={
            "keyword": keyword,
            "count": count
        }
    )