from animals.animal import Animal
from logging_config import Logger

logger = Logger()


class AnimalCage:
    def __init__(self):
        self._animals_in_cage: list[Animal] = []
        logger.info(f"initialized animal cage")
        logger.debug("Animal cage created with empty list")

    def __add__(self, animal):
        """
        Function to add an animal to the animals_in_cage
        :param animal: Animal to add to the animals_in_cage
        Usage: cage + animal
        """
        logger.debug(f"__add__ called with: {animal}")
        self._animals_in_cage.append(animal)
        logger.info(f"Added animal to animal cage")
        logger.debug(f"Cage now contains {len(self._animals_in_cage)} animals")
        return self

    def __sub__(self, animal):
        """
        Function to remove an animal from the animals_in_cage
        :param animal: Animal to remove from the animals_in_cage
        """
        logger.debug(f"__sub__ called with: {animal}")
        if animal in self._animals_in_cage:
            self._animals_in_cage.remove(animal)
            logger.info(f"Removed animal {animal} from cage")
            logger.debug(f"Cage now contains {len(self._animals_in_cage)} animals")
        else:
            logger.info(f"failed to remove animal from cage")
        return self

    def __len__(self):
        """
        Function to return the amount of animals in the animals_in_cage
        :return: Amount of animals in the animals_in_cage
        """
        return len(self.animals_in_cage)

    def __iadd__(self, other_cage):
        """
        Function adds another animal cage to current cage
        :param other_cage: cage to add to current cage
        :return: original cage, with added members from second cage
        Usage: cage_1 += cage_2
        """
        logger.debug(f"Merging cage with {len(other_cage)} animals into current cage")
        self._animals_in_cage.extend(other_cage.animals_in_cage)
        logger.info("Cages merged successfully")
        logger.debug(f"Cage now contains {len(self._animals_in_cage)} animals")
        return self

    def __str__(self):
        """
        Display the animals in the animals_in_cage for the user
        """
        if not self.animals_in_cage:
            return "Animal cage is empty"
        animal_strings = [str(animal) for animal in self._animals_in_cage]
        return f"AnimalCage with {len(self._animals_in_cage)} animals:\n" + "\n".join(animal_strings)

    def __repr__(self):
        """
        Function to print animals to developer
        """
        return f"AnimalCage(animals_in_cage={self._animals_in_cage!r})"

    @property
    def animals_in_cage(self):
        return self._animals_in_cage

    @animals_in_cage.setter
    def animals_in_cage(self, value):
        if not isinstance(value, list):
            raise ValueError("Must be a list of Animal objects")
        self._animals_in_cage = value
