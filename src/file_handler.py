class FileHandler:
    @staticmethod
    def file_to_list(file_path):
        """
        Function turns given text file into list of words
        :param file_path: Path to file
        :return: List of words from file
        """
        words_from_file = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    words_from_file += line.split()

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Unknown file: {e}")

        return words_from_file
