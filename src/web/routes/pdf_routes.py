from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates

from src.services.file_service import save_uploaded_file
from src.services.pdf_service import extract_text_from_pdf

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
    content = await pdf_file.read()

    file_path = save_uploaded_file(
        pdf_file.filename,
        content
    )

    extracted_text = extract_text_from_pdf(
        file_path
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "extracted_text": extracted_text
        }
    )