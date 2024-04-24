import logging
import sys


class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.file_handler = logging.FileHandler('app.log')

        self.stream_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)

        self.logger.handlers = [self.stream_handler, self.file_handler]
        self.logger.setLevel(logging.INFO)
