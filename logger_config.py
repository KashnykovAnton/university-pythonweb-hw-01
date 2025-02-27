import logging
from colorama import Fore


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "WARNING": Fore.YELLOW,
        "INFO": Fore.GREEN,
        "ERROR": Fore.RED,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        return f"{color}{record.levelname}: {record.msg}{Fore.RESET}"


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter())

logger.addHandler(handler)
