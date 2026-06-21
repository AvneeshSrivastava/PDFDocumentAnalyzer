from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.exceptions import PDFAnalyzerException
from src.exceptions.handlers import pdf_exception_handler
from src.logging import logger
from src.web.routes.health_routes import router as health_router
from src.web.routes.pdf_routes import router as pdf_router


app = FastAPI(
    title="PDF Document Analyzer",
    description="AI ML Road Map - Phase 1",
    version="1.0.0"
)

# Register Static Files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Register Exception Handlers
app.add_exception_handler(
    PDFAnalyzerException,
    pdf_exception_handler
)

# Register API Routes
app.include_router(pdf_router)
app.include_router(health_router)

logger.info("Application started successfully.")