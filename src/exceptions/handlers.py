from fastapi import Request
from fastapi.templating import Jinja2Templates

from src.config import settings
from src.exceptions import PDFAnalyzerException
from src.logging import logger

# ==========================================================
# Template Configuration
# ==========================================================

# Initialize the Jinja2 template engine.
# This is used to render HTML pages returned by the exception handler.
templates = Jinja2Templates(
    directory=settings.TEMPLATE_FOLDER
)


# ==========================================================
# Global Exception Handler
# ==========================================================

async def pdf_exception_handler(
    request: Request,
    exc: PDFAnalyzerException
):
    """
    Handle all application-specific exceptions.

    This global exception handler catches every exception derived
    from PDFAnalyzerException, logs the error details, and returns
    a user-friendly error page.

    Parameters
    ----------
    request : Request
        Current HTTP request.

    exc : PDFAnalyzerException
        Application-specific exception that occurred.

    Returns
    -------
    TemplateResponse
        Renders the error.html template with an appropriate
        error message and HTTP status code.
    """

    # ------------------------------------------------------
    # Log the exception for troubleshooting and auditing.
    # ------------------------------------------------------

    logger.error(
        "Application Error: %s",
        str(exc)
    )

    # ------------------------------------------------------
    # Render the error page.
    # ------------------------------------------------------

    return templates.TemplateResponse(
        request=request,
        name="error.html",
        context={
            "message": str(exc)
        },
        status_code=400
    )