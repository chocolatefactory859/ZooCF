from __future__ import annotations
import sys

from logging_config import Logger

ORIGINAL_STDOUT = sys.stdout
logger = Logger()


class Toilet:
    def __init__(self, toilet_output_path):
        self.toilet_output_path = toilet_output_path
        self.lid_state: bool = False
        self.output_file = open(self.toilet_output_path, 'a')

    def open_lid(self):
        """
        Changes stdout to file
        """
        self.lid_state = True
        sys.stdout = self.output_file
        logger.info("Opened toilet lid")

    def close_lid(self):
        """
        Changes stdout back to original
        """
        self.lid_state = False
        sys.stdout = ORIGINAL_STDOUT
        logger.info("Closed toilet lid")

    def flush_toilet(self):
        """
        Flush toilet contents
        """
        sys.stdout = ORIGINAL_STDOUT
        self.output_file.close()
        open(self.toilet_output_path, 'w').close()
        self.output_file = open(self.toilet_output_path, 'a')
        logger.info("Flushed toilet")
        sys.stdout = self.output_file

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
        self.output_file.close()
