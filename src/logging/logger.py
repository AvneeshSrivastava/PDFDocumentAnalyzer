import logging
import os

from src.config.settings import settings

# ==========================================================
# Log Directory Configuration
# ==========================================================

# Create the log directory if it does not already exist.
# This ensures that log files can be created successfully
# even when the application is executed for the first time.
os.makedirs(
    settings.LOG_FOLDER,
    exist_ok=True
)

# Full path of the application log file.
LOG_FILE = os.path.join(
    settings.LOG_FOLDER,
    "application.log"
)

# ==========================================================
# Logger Configuration
# ==========================================================

# Create a named logger using the application name.
logger = logging.getLogger(
    settings.APP_NAME
)

# Set the minimum logging level.
logger.setLevel(
    logging.INFO
)

# ==========================================================
# Log Message Format
# ==========================================================

# Common formatter used by both console and file handlers.
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# ==========================================================
# Console Handler
# ==========================================================

# Displays log messages in the terminal.
console_handler = logging.StreamHandler()

console_handler.setFormatter(
    formatter
)

# ==========================================================
# File Handler
# ==========================================================

# Writes log messages to the application log file.
file_handler = logging.FileHandler(
    LOG_FILE
)

file_handler.setFormatter(
    formatter
)

# ==========================================================
# Register Handlers
# ==========================================================

# Prevent duplicate handlers when FastAPI auto-reloads
# during development.
if not logger.handlers:

    logger.addHandler(
        console_handler
    )

    logger.addHandler(
        file_handler
    )