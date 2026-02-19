from src.input.file_reader import FileReader


class TextFileReader(FileReader):
    @staticmethod
    def parse_input_to_word(file_path: str) -> list:
        """
        Function turns given text file into list of words
        Param: file_path: Path to file
        Return: List of words from file
        Raise: FileNotFoundError
        """
        with open(file_path, 'r') as file:
            return file.read().split()
