from abc import ABC, abstractmethod


class FileReader(ABC):
    @staticmethod
    @abstractmethod
    def parse_input_to_words(input_path: str):
        """
        Function reads input from input path
        """
        pass
