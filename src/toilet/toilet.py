from __future__ import annotations
import os
import sys

from logging_config import Logger

ORIGINAL_STDOUT = sys.stdout
logger = Logger()


class Toilet:
    def __init__(self):
        self.lid_state: bool = False

        toilet_output_filepath = os.getenv("TOILET_OUTPUT")
        self.output_file = open(toilet_output_filepath, 'a')

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
        open(os.getenv("TOILET_OUTPUT"), 'w').close()
        self.output_file = open(os.getenv("TOILET_OUTPUT"), 'a')
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
