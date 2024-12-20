import logging

class CustomFormatter(logging.Formatter):
    grey = "\33[38;20m"
    yellow = "\33[33;20m"
    red = "\33[31;20m"
    bold_red = "\33[31;1m"
    reset = "\33[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)

# ANSI ESC SGR
escSeqStart = "\33["
sgrReset = "0m"
class foregroundColor():
    black = escSeqStart + "30m"
    red = escSeqStart + "31m"
    green = escSeqStart + "32m"
    yellow = escSeqStart + "33m"
    blue = escSeqStart + "34m"
    magenta = escSeqStart + "35m"
    cyan = escSeqStart + "36m"
    white = escSeqStart + "37m"
    brightBlack = escSeqStart + "90m"
    gray = brightBlack
    grey = brightBlack
    brightRed = escSeqStart + "91m"
    brightGreen = escSeqStart + "92m"
    brightyellow = escSeqStart + "93m"
    brightblue = escSeqStart + "94m"
    brightmagenta = escSeqStart + "95m"
    brightcyan = escSeqStart + "96m"
    brightwhite = escSeqStart + "97m"
    reset = escSeqStart + sgrReset