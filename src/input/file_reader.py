from abc import ABC, abstractmethod


class FileReader(ABC):
    @staticmethod
    @abstractmethod
    def read_input_to_words(input_path: str) -> list[str]:
        """
        Function reads input from input path
        """
        pass
