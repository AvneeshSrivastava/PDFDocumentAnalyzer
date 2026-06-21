import os


class BaseConfig:
    """
    Base application configuration.

    This class contains all application-wide settings that are shared
    across different environments (Development, Testing, Production).

    Centralizing configuration makes the application easier to maintain
    and avoids hardcoded values throughout the project.
    """

    # ==========================================================
    # Application Information
    # ==========================================================

    APP_NAME = "PDF Document Analyzer"
    APP_VERSION = "1.0.0"

    # ==========================================================
    # Project Root Directory
    # ==========================================================

    # Root directory of the project.
    # Example:
    # PDFDocumentAnalyzer/
    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    # ==========================================================
    # Data Directories
    # ==========================================================

    # Root folder used for application data.
    DATA_FOLDER = os.path.join(
        PROJECT_ROOT,
        "data"
    )

    # Folder containing uploaded/input PDF files.
    INPUT_FOLDER = os.path.join(
        DATA_FOLDER,
        "input"
    )

    # Folder used to store generated output files.
    OUTPUT_FOLDER = os.path.join(
        DATA_FOLDER,
        "output"
    )

    # ==========================================================
    # Web Resources
    # ==========================================================

    # HTML templates directory.
    TEMPLATE_FOLDER = os.path.join(
        PROJECT_ROOT,
        "templates"
    )

    # Static resources (CSS, JavaScript, Images).
    STATIC_FOLDER = os.path.join(
        PROJECT_ROOT,
        "static"
    )

    # Upload directory used by the application.
    UPLOAD_FOLDER = os.path.join(
        PROJECT_ROOT,
        "uploads"
    )

    # Log files directory.
    LOG_FOLDER = os.path.join(
        PROJECT_ROOT,
        "logs"
    )

    # ==========================================================
    # File Validation Settings
    # ==========================================================

    # Allowed file extensions.
    ALLOWED_FILE_EXTENSIONS = (
        ".pdf",
    )

    # Allowed MIME content types.
    ALLOWED_CONTENT_TYPES = (
        "application/pdf",
    )

    # Maximum allowed upload size (in MB).
    MAX_FILE_SIZE_MB = 10