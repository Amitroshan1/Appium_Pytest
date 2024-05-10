import logging
from datetime import datetime


class LogGen:
    @staticmethod
    def setup_logger(log_file='.\\logs\\automation.log'):
        """Set up logging configuration."""

        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger