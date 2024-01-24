import logging
import os


class Log:

    def __init__(self, name, level=logging.DEBUG, log_file="lp3d.log"):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Handler for file output
        self._file_handler = logging.FileHandler(log_file, mode='a')
        self._file_handler.setFormatter(self._formatter)

        # Handler for console output
        self._stream_handler = logging.StreamHandler()
        self._stream_handler.setFormatter(self._formatter)

        self._logger.addHandler(self._file_handler)
        self._logger.addHandler(self._stream_handler)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.error(message)

