from abc import ABC, abstractmethod


class InputParser(ABC):
    @abstractmethod
    def parse_input(self):
        pass