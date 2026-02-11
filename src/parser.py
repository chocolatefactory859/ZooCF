import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("filename", help="Please enter file path to read animal names from")

    def parse_input(self):
        args = self.parser.parse_args()
        return vars(args)
