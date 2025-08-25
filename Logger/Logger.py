import os
import logging


class Logger:
    def __init__(self, name):
        self.log_file = os.path.join(os.environ["PYTHONPATH"], "Logger/log.log")
        self.level = logging.DEBUG
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.level)
        self.format = "%(asctime)s - %(levelname)s - %(message)s"

        # Console handler for output to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)
        console_formatter = logging.Formatter(self.format)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # File handler for output to a log file
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.level)
        file_formatter = logging.Formatter(self.format)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """Return the logger object so the user can log directly."""
        return self.logger