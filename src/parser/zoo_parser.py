import argparse

from src.parser.input_parser import InputParser


class ZooParser(InputParser):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("filepath", help="Please enter file path to read animal names from")

    def parse_to_words(self):
        """
        Function parses input according to decided parameters
        :return: Parsed arguments
        """
        args = self.parser.parse_args()
        return vars(args)
