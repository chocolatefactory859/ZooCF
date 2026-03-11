from typing import IO

from animals.animal import Animal
from objects.object_instance_factory import ObjectInstanceFactory


class AnimalGenerator2:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self._file: IO = None
        self._words_from_file: list[str] = []
        self._index: int = 0

    def __iter__(self):
        """
        Opens the file and resets internal state for iteration
        return: The AnimalGenerator instance as an iterator
        """
        self._file = open(self.file_path, "r")
        self._words_from_file = []
        self._index = 0
        return self

    def __next__(self) -> Animal:
        """
        Creates Animal object from words in file
        return: Created Animal object
        raise: StopIteration, Stops when all animals have been generated
        """
        while self._index >= len(self._words_from_file):
            line = self._file.readline()
            if not line:
                self._file.close()
                raise StopIteration
            self._words_from_file = line.strip().split()
            self._index = 0

        animal_name = self._words_from_file[self._index]
        self._index += 1
        return ObjectInstanceFactory.create_object(animal_name, animal_name)
