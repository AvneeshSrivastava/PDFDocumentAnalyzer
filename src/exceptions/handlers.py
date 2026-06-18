from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.config import settings
from src.logging import logger
from src.exceptions import PDFAnalyzerException

templates = Jinja2Templates(
    directory=settings.TEMPLATE_FOLDER
)


async def pdf_exception_handler(
    request: Request,
    exc: PDFAnalyzerException
):

    logger.error(
        str(exc)
    )

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": str(exc)
        },
        status_code=400
    )