import os

from src.config import settings
from src.exceptions import FileStorageException
from src.logging import logger


def save_uploaded_file(
    file_name: str,
    content: bytes
) -> str:
    """
    Save an uploaded PDF file to the configured upload directory.

    This function is responsible for creating the upload directory
    (if it does not already exist) and writing the uploaded file
    to disk.

    Parameters
    ----------
    file_name : str
        Name of the uploaded PDF file.

    content : bytes
        Binary content of the uploaded file.

    Returns
    -------
    str
        Absolute path of the saved PDF file.

    Raises
    ------
    FileStorageException
        Raised when the uploaded file cannot be saved.
    """

    try:

        # ==========================================================
        # Log Upload Request
        # ==========================================================

        logger.info(
            "Saving uploaded file: %s",
            file_name
        )

        # ==========================================================
        # Create Upload Directory
        # ==========================================================

        # Create the upload folder if it does not exist.
        os.makedirs(
            settings.UPLOAD_FOLDER,
            exist_ok=True
        )

        # ==========================================================
        # Build Destination File Path
        # ==========================================================

        file_path = os.path.join(
            settings.UPLOAD_FOLDER,
            file_name
        )

        # ==========================================================
        # Save Uploaded File
        # ==========================================================

        with open(file_path, "wb") as file:
            file.write(
                content
            )

        # ==========================================================
        # Log Success
        # ==========================================================

        logger.info(
            "File saved successfully: %s",
            file_path
        )

        return file_path

    except Exception as ex:
        # ==========================================================
        # Log Failure
        # ==========================================================
        logger.error(
            "Failed to save uploaded file: %s",
            file_name,
            exc_info=True
        )

        raise FileStorageException(
            "Unable to save the uploaded PDF file."
        ) from ex