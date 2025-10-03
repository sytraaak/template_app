import logging
import sys
from pathlib import Path
from .config import settings

def setup_logging() -> logging.Logger:
    log_file = Path(settings.logging.file_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # Zamezení duplikovaným handlerům při opakování
    if root.handlers:
        return root

    # Console
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(settings.logging.console_level.upper())
    ch.setFormatter(logging.Formatter(settings.logging.console_format))
    root.addHandler(ch)

    # File
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(settings.logging.file_level.upper())
    fh.setFormatter(logging.Formatter(settings.logging.file_format))
    root.addHandler(fh)

    return root
