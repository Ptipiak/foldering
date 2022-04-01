__version__ = "0.1.0"

import os
import logging

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")

# Create the Logger
logger = logging.getLogger(__name__)
# Set the logger level
logger.setLevel(logging.INFO)
# Create the Handler for logging data to a file
handler = logging.StreamHandler()
# Set the handler loggers level
handler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
if DEBUG:
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
# Formatter for log messages
formatter = logging.Formatter(
    "%(levelname)s - %(asctime)s - %(name)s: %(message)s", "%H:%M:%S"
)
# Set handler formatter
handler.setFormatter(formatter)
# Add the Handler to the Logger
logger.addHandler(handler)

if DEBUG:
    logger.warn("Debug mode is on")

__all__ = ["main"]
