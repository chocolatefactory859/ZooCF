from __future__ import annotations
import sys
from typing import IO

from logging_config import Logger

logger = Logger()


class Toilet:
    def __init__(self, toilet_output_path: str):
        self._default_stdout: IO = sys.stdout
        self._toilet_output_path: str = toilet_output_path
        self._lid_state: bool = False
        self._output_file: IO = None

    def open_lid(self):
        """
         Opens the toilet lid and redirect standard output to the toilet file
        """
        self._lid_state = True
        self._output_file = open(self._toilet_output_path, 'a')

        sys.stdout = self._output_file
        logger.info("Opened toilet lid")

    def close_lid(self):
        """
        Changes stdout back to original
        """
        self._lid_state = False
        sys.stdout = self._default_stdout

        self._output_file.close()
        logger.info("Closed toilet lid")

    def flush_toilet(self):
        """
        Flush toilet contents
        """
        self._output_file.seek(0)
        self._output_file.truncate()

        logger.info("Flushed toilet")

    def __enter__(self) -> Toilet:
        """
         Opens the toilet lid and returns the current Toilet instance
        :return: Open toilet
        """
        self.open_lid()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Defines what happens when toilet is exited
        :param exc_type: Exception type
        :param exc_val: Exception instance raised
        :param exc_tb: Exception traceback
        """
        self.close_lid()
        if exc_type is not None:
            logger.error(f"Error occurred: {exc_val}")

        return False
