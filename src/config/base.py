import os


class BaseConfig:
    """
    Base application configuration.

    This class contains settings shared across
    all environments.
    """

    # Application
    APP_NAME = "PDF Document Analyzer"
    APP_VERSION = "0.3.0"

    # Project Root Directory
    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    # Data Directories
    DATA_FOLDER = os.path.join(
        PROJECT_ROOT,
        "data"
    )

    INPUT_FOLDER = os.path.join(
        DATA_FOLDER,
        "input"
    )

    OUTPUT_FOLDER = os.path.join(
        DATA_FOLDER,
        "output"
    )

    # Template Directory
    TEMPLATE_FOLDER = os.path.join(
        PROJECT_ROOT,
        "templates"
    )

    # Static Directory
    STATIC_FOLDER = os.path.join(
        PROJECT_ROOT,
        "static"
    )

    # File Upload Configuration
    ALLOWED_FILE_EXTENSIONS = (
        ".pdf",
    )

    MAX_FILE_SIZE_MB = 10