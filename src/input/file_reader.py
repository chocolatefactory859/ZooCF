from abc import ABC, abstractmethod


class FileReader(ABC):
    @staticmethod
    @abstractmethod
    def read_input(input_path: str):
        """
        Function reads input from input path
        """
        pass
