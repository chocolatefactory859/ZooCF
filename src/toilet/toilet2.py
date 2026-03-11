from __future__ import annotations
import sys
from contextlib import contextmanager
from typing import IO

from logging_config import Logger

logger = Logger()


class Toilet2:
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

    @contextmanager
    def toilet_context(toilet_output_path: str) -> Toilet:
        """
        Function-based context manager for Toilet.

        Opens the toilet lid and redirects stdout to the toilet file.
        Ensures the lid is closed even if an exception occurs.

        :param toilet_output_path: Path to the toilet output file.
        :yield: Toilet instance.
        """
        toilet = Toilet2(toilet_output_path)
        try:
            toilet.open_lid()
            yield toilet
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            raise
        finally:
            toilet.close_lid()
