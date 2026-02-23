from abc import ABC, abstractmethod


class InputParser:
    @abstractmethod
    def parse_input(self):
        """
        Function parses input
        Specifics depend on implementing class
        """
        pass