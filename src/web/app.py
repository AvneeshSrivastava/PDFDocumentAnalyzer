from fastapi import UploadFile, File
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from src.services.file_service import save_uploaded_file

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/upload")    
async def upload_pdf(pdf_file: UploadFile = File(...)):

    content = await pdf_file.read()

    file_path = save_uploaded_file(
        pdf_file.filename,
        content
    )

    return {
        "message": "File uploaded successfully",
        "file_path": file_path
    }
