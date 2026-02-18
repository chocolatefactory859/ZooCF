from src.input.file_reader import FileReader


class TextFileReader(FileReader):
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
            print(f"Error: {error}")
