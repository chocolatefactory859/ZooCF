from input.file_reader import FileReader


class TextFileReader(FileReader):
    @staticmethod
    def read_input_to_words(file_path: str) -> list[str]:
        """
        Function turns given text file into list of words
        Param: file_path: Path to file
        Return: List of words from file
        Raise: FileNotFoundError
        """
        with open(file_path, 'r') as file:
            return file.read().split()
