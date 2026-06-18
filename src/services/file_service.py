import os

from src.config import settings
from src.exceptions.custom_exceptions import FileStorageException
from src.logging import logger


def save_uploaded_file(file_name, content):
    """
    Save the uploaded PDF into the configured input folder.
    """
    try:
        logger.info("Saving uploaded file: %s", file_name)

        upload_dir = settings.INPUT_FOLDER

        os.makedirs(
            upload_dir,
            exist_ok=True
        )

        file_path = os.path.join(
            upload_dir,
            file_name
        )

        with open(file_path, "wb") as file:
            file.write(content)

        logger.info(
            "File saved successfully: %s",
            file_path
        )

        return file_path

    except Exception as ex:
        logger.error(
            "Failed to save uploaded file: %s",
            file_name,
            exc_info=True
        )

        raise FileStorageException(
            "Unable to save uploaded file."
        ) from ex