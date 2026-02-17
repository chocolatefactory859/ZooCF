from abc import ABC, abstractmethod


class FileHandler(ABC):
    @staticmethod
    @abstractmethod
    def read_input(input_path: str):
        """
        Function reads input from input path
        """
        pass
