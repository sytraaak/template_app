import logging
from src.config import settings

logger = logging.getLogger(__name__)

def run():
    if not settings.secrets.gol_password or not settings.secrets.gol_username:
        logger.warning("Chybí API_KEY v .env")

run()