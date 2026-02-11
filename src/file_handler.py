class FileHandler:
    @staticmethod
    def file_to_list(file_path):
        words_from_file = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    words_from_file += line.split()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Unknown file: {e}")

        return words_from_file
