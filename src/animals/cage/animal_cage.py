from __future__ import annotations

from animals.animal import Animal
from logging_config import Logger

logger = Logger()


class AnimalCage:
    def __init__(self):
        self._animals_in_cage: list[Animal] = []
        logger.info("Initialized animal cage")

    def __add__(self, other: Animal | AnimalCage) -> AnimalCage:
        """
        Add an animal or merge another cage into this cage.

        :param other: Animal or AnimalCage to add
        :raises TypeError: if other is not an Animal or AnimalCage
        :return: Self (the cage after addition)
        """
        if isinstance(other, Animal):
            logger.debug(" Trying to add %s to cage", other)
            self._animals_in_cage.append(other)
            return self

        elif isinstance(other, AnimalCage):
            logger.debug("Trying to add %d animals to animal cage", len(other.animals_in_cage))
            new_cage = AnimalCage()
            new_cage._animals_in_cage = (self._animals_in_cage.copy() + other.animals_in_cage.copy())
            return new_cage

        raise TypeError(f"Can only add Animal or AnimalCage, not {type(other)}")

    def __sub__(self, animal: Animal) -> AnimalCage:
        """
        Remove an animal from the cage.

        :param animal: Animal to remove from the cage
        :raises ValueError: if the animal is not in the cage
        """
        logger.info("Trying to remove %s from cage", animal)
        try:
            self._animals_in_cage.remove(animal)
            logger.debug("Removed animal %s from cage", animal)

        except ValueError:
            logger.error("Failed to remove animal %s: not in cage", animal)
            raise ValueError(f"Animal {animal} is not in the cage")

        logger.debug("Cage now contains %d animals", len(self._animals_in_cage))
        return self

    def __len__(self) -> int:
        """
        Return the amount of animals in the animals_in_cage

        :return: Amount of animals in the animals_in_cage
        """
        return len(self.animals_in_cage)

    def __str__(self) -> str:
        """
        Display the animals in the animals_in_cage for the user
        """
        if not self.animals_in_cage:
            return "Animal cage is empty"

        animal_strings = [str(animal) for animal in self._animals_in_cage]
        return f"AnimalCage with {len(self._animals_in_cage)} animals:\n" + "\n".join(animal_strings)

    def __repr__(self) -> str:
        """
        Print animals to developer
        """
        return f"AnimalCage(animals_in_cage={self._animals_in_cage!r})"

    @property
    def animals_in_cage(self) -> list[Animal]:
        return self._animals_in_cage

    @animals_in_cage.setter
    def animals_in_cage(self, animals_to_put_in_cage: list[Animal]) -> None:
        if not isinstance(animals_to_put_in_cage, list):
            raise ValueError("Must be a list of Animal objects")
        self._animals_in_cage = animals_to_put_in_cage
