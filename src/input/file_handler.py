from src.input.input_handler import InputHandler


class FileHandler(InputHandler):
    @staticmethod
    def read_input(file_path: str) -> list:
        """
        Function turns given text file into list of words
        :param file_path: Path to file
        :return: List of words from file
        """
        try:
            with open(file_path, 'r') as file:
                words_from_file = file.read().split()

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Unknown file: {e}")

        return words_from_file
