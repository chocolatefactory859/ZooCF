import argparse

from src.parser.input_parser import InputParser


class ZooParser(InputParser):
    def __init__(self):
        """
        Initiate class
        """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("filename", help="Please enter file path to read animal names from")

    def parse_input(self):
        """
        Function parses input according to decided parameters
        :return: Parsed arguments
        """
        args = self.parser.parse_args()
        return vars(args)
