import argparse

from src.parser.input_parser import InputParser


class ZooParser(InputParser):
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ZooParser, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
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
