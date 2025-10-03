from __future__ import annotations
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict
from dotenv import load_dotenv
import tomllib

# --- Lokace rootu a souborů ---
BASE_DIR = Path(__file__).resolve().parent  # .../project-root/src
ROOT_DIR = BASE_DIR.parent                      # .../project-root
DOTENV_PATH = ROOT_DIR / ".env"
TOML_PATH = ROOT_DIR / "config.toml"

# --- LOAD ENV ---
load_dotenv(DOTENV_PATH)

# --- Načti TOML (netajné) ---
def _load_toml(path: Path) -> Dict[str, Any]:
    with path.open("rb") as f:
        return tomllib.load(f)

_cfg = _load_toml(TOML_PATH)

# --- TOML ---
@dataclass(frozen=True)
class AppConfig:
    pass

@dataclass(frozen=True)
class LoggingConfig:
    console_level: str  = str(_cfg.get("logging", {}).get("console_level", "INFO"))
    file_level: str     = str(_cfg.get("logging", {}).get("file_level", "DEBUG"))
    file_path: str      = str(_cfg.get("logging", {}).get("file_path", "logs/app.log"))
    console_format: str = str(_cfg.get("logging", {}).get("console_format", "%(message)s"))
    file_format: str    = str(_cfg.get("logging", {}).get("file_format", "%(message)s"))

# --- ENV ---
@dataclass(frozen=True)
class Secrets:
    gol_username: str = os.getenv("GOL_USERNAME", "")
    gol_password: str = os.getenv("GOL_PASSWORD", "")

# --- Settings ---
class Settings:
    BASE_DIR  = BASE_DIR
    ROOT_DIR  = ROOT_DIR
    dotenv    = DOTENV_PATH
    toml      = TOML_PATH

    app       = AppConfig()
    logging   = LoggingConfig()
    secrets   = Secrets()

settings = Settings()