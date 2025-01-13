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
controlSequenceIntroducer = "\33["
sgrReset = "0m"

class baseColors():
    black = "0"
    red = "1"
    green = "2"
    yellow = "3"
    blue = "4"
    magenta = "5"
    cyan = "6"
    white = "7"

class foregroundColor():
    black = f"{controlSequenceIntroducer}3{baseColors.black}m"
    red = f"{controlSequenceIntroducer}3{baseColors.red}m"
    green = f"{controlSequenceIntroducer}3{baseColors.green}m"
    yellow = f"{controlSequenceIntroducer}3{baseColors.yellow}m"
    blue = f"{controlSequenceIntroducer}3{baseColors.blue}m"
    magenta = f"{controlSequenceIntroducer}3{baseColors.magenta}m"
    cyan = f"{controlSequenceIntroducer}3{baseColors.cyan}m"
    white = f"{controlSequenceIntroducer}3{baseColors.white}m"
    brightBlack = gray = grey = f"{controlSequenceIntroducer}9{baseColors.black}m"
    brightRed = f"{controlSequenceIntroducer}9{baseColors.red}m"
    brightGreen = f"{controlSequenceIntroducer}9{baseColors.green}m"
    brightyellow = f"{controlSequenceIntroducer}9{baseColors.yellow}m"
    brightblue = f"{controlSequenceIntroducer}9{baseColors.blue}m"
    brightmagenta = f"{controlSequenceIntroducer}9{baseColors.magenta}m"
    brightcyan = f"{controlSequenceIntroducer}9{baseColors.cyan}m"
    brightwhite = f"{controlSequenceIntroducer}9{baseColors.white}m"
    reset = controlSequenceIntroducer + sgrReset

class backgroundColor():
    black = f"{controlSequenceIntroducer}4{baseColors.black}m"
    red = f"{controlSequenceIntroducer}4{baseColors.red}m"
    green = f"{controlSequenceIntroducer}4{baseColors.green}m"
    yellow = f"{controlSequenceIntroducer}4{baseColors.yellow}m"
    blue = f"{controlSequenceIntroducer}4{baseColors.blue}m"
    magenta = f"{controlSequenceIntroducer}4{baseColors.magenta}m"
    cyan = f"{controlSequenceIntroducer}4{baseColors.cyan}m"
    white = f"{controlSequenceIntroducer}4{baseColors.white}m"
    brightBlack = gray = grey = f"{controlSequenceIntroducer}10{baseColors.black}m"
    brightRed = f"{controlSequenceIntroducer}10{baseColors.red}m"
    brightGreen = f"{controlSequenceIntroducer}10{baseColors.green}m"
    brightyellow = f"{controlSequenceIntroducer}10{baseColors.yellow}m"
    brightblue = f"{controlSequenceIntroducer}10{baseColors.blue}m"
    brightmagenta = f"{controlSequenceIntroducer}10{baseColors.magenta}m"
    brightcyan = f"{controlSequenceIntroducer}10{baseColors.cyan}m"
    brightwhite = f"{controlSequenceIntroducer}10{baseColors.white}m"
    reset = controlSequenceIntroducer + sgrReset