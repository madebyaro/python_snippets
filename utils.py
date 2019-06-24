"""util.py
    common utilities
"""

import time
import os
import json
import uuid
from logging import Logger, StreamHandler, Formatter, getLogger
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
"""

log_levels = {
    'CRITICAL': CRITICAL,
    'ERROR': ERROR,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET
}

def make_logger(name: str) -> Logger:
    log_level_name = os.environ.get('LOG_LEVEL')
    log_level = log_levels.get(log_level_name, NOTSET)

    # Look up or create Logger
    logger = getLogger(name)

    # If this is a new object, set up a handler
    if not logger.handlers:
        log_handler = StreamHandler()
        log_formatter = Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        log_handler.setFormatter(log_formatter)
        logger.addHandler(log_handler)
        logger.setLevel(log_level)

    return logger

def timestamp() -> int:
    return int(time.time() * 1000000)
