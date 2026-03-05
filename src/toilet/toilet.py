from __future__ import annotations
import sys

from logging_config import Logger

logger = Logger()


class Toilet:
    def __init__(self, toilet_output_path):
        self.default_stdout = sys.stdout
        self.toilet_output_path = toilet_output_path
        self.lid_state: bool = False
        self.output_file = None

    def open_lid(self):
        """
        Changes stdout to file
        """
        self.lid_state = True
        self.output_file = open(self.toilet_output_path, 'a')
        sys.stdout = self.output_file
        logger.info("Opened toilet lid")

    def close_lid(self):
        """
        Changes stdout back to original
        """
        self.lid_state = False
        sys.stdout = self.default_stdout
        self.output_file.close()
        logger.info("Closed toilet lid")

    def flush_toilet(self):
        """
        Flush toilet contents
        """
        self.output_file.seek(0)
        self.output_file.truncate()

        logger.info("Flushed toilet")

    def __enter__(self) -> Toilet:
        """
        Defines what happens when toilet is called
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
