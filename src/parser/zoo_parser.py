import argparse

from src.parser.input_parser import InputParser
from src.parser.singleton_meta import SingletonMeta


class ZooParser(InputParser, metaclass=SingletonMeta):
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='Parses arguments from user, according to given flags')
        self.parser.add_argument("filepath", help="Please enter file path to read animal names from")

    def parse_input(self) -> dict[str, any]:
        """
        Function parses input according to decided parameters
        Return: Parsed arguments
        """
        args = self.parser.parse_args()
        return vars(args)
