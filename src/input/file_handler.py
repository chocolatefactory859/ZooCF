from src.input.input_handler import FileHandler


class TextFileHandler(FileHandler):
    @staticmethod
    def read_input(file_path: str) -> list:
        """
        Function turns given text file into list of words
        Param: file_path: Path to file
        Return: List of words from file
        Raise: FileNotFoundError
        """
        try:
            with open(file_path, 'r') as file:
                return file.read().split()

        except FileNotFoundError as error:
            raise FileNotFoundError(f"Unknown file, {file_path}: {error}")

