import logging
import os

from src.config.settings import settings

# Create logs directory if it does not exist
os.makedirs(
    os.path.join(settings.PROJECT_ROOT, "logs"),
    exist_ok=True
)

LOG_FILE = os.path.join(
    settings.PROJECT_ROOT,
    "logs",
    "application.log"
)

logger = logging.getLogger(settings.APP_NAME)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Console Logger
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Logger
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

# Avoid duplicate handlers during FastAPI reload
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)