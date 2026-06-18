from fastapi import FastAPI

from src.exceptions import PDFAnalyzerException
from src.exceptions.handlers import pdf_exception_handler
from src.logging import logger
from src.web.routes.pdf_routes import router

app = FastAPI()

app.add_exception_handler(
    PDFAnalyzerException,
    pdf_exception_handler
)

logger.info("Application started successfully.")

app.include_router(router)