from __future__ import annotations
import sys
from typing import TextIO

ORIGINAL_STDOUT = sys.stdout


class Toilet:
    def __init__(self):
        self.lid_state: bool = False
        self.output_file: TextIO = open("toilet_output.txt", 'w')

    def open_lid(self) -> None:
        """
        Changes stdout to file
        """
        self.lid_state = True
        sys.stdout = self.output_file

    def close_lid(self) -> None:
        """
        Changes stdout back to original
        """
        self.lid_state = False
        sys.stdout = ORIGINAL_STDOUT

    def __enter__(self) -> Toilet:
        """
        Defines what happens when toilet is called
        :return: Open toilet
        """
        self.open_lid()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Defines what happens when toilet is exited
        :param exc_type: Exception type
        :param exc_val: Exception instance raised
        :param exc_tb: Exception traceback
        """
        self.close_lid()
