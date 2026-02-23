from abc import ABC, abstractmethod

from src.parser.singleton_meta import SingletonMeta


class InputParser(metaclass=SingletonMeta):
    @abstractmethod
    def parse_input(self):
        """
        Function parses input
        Specifics depend on implementing class
        :return:
        """
        pass