from fastapi import FastAPI

from src.exceptions import PDFAnalyzerException
from src.exceptions.handlers import pdf_exception_handler
from src.logging import logger
from src.web.routes.pdf_routes import router
from src.web.routes.health_routes import router as health_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_exception_handler(
    PDFAnalyzerException,
    pdf_exception_handler
)

logger.info("Application started successfully.")

app.include_router(router)
app.include_router(health_router)