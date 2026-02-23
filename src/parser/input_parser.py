from abc import ABC, abstractmethod


class InputParser:
    @abstractmethod
    def parse_input(self) -> dict[str, any]:
        """
        Function parses input
        Specifics depend on implementing class
        """
        pass