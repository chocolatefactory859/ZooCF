import argparse

from src.parser.input_parser import InputParser


class ZooParser(InputParser):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("filepath", help="Please enter file path to read animal names from")
        self._initialized = True

    def parse_input(self) -> dict:
        """
        Function parses input according to decided parameters
        Return: Parsed arguments
        """
        args = self.parser.parse_args()
        return vars(args)
