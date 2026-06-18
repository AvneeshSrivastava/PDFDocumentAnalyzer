import os
from src.config import settings
from src.logging import logger
def save_uploaded_file(file_name, content):
    """
    Save the uploaded PDF into the project's data/input folder.
    """
    logger.info("Saving uploaded file: %s", file_name)
    # Project Root Directory
    project_root = settings.INPUT_FOLDER

    # Folder where uploaded PDFs are stored
    upload_dir = os.path.join(
        project_root,
        "data",
        "input"
    )
    # Create folder if it does not exist
    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    # Full file path
    file_path = os.path.join(
        upload_dir,
        file_name
    )
    logger.info(
        "Saving uploaded file: %s",
        file_name
    )
    # Save uploaded file
    with open(file_path, "wb") as file:
        file.write(content)

    logger.info("File saved successfully: %s", file_path)
    return file_path