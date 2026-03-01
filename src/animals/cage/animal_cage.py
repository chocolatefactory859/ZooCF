from animals.animal import Animal
from logging_config import Logger

logger = Logger()


class AnimalCage:
    def __init__(self):
        self.animals_in_cage: list[Animal] = []
        logger.get_logger().info(f"initialized animal cage")

    def __add__(self, animal):
        """
        Function to add an animal to the animals_in_cage
        :param animal: Animal to add to the animals_in_cage
        """
        self.animals_in_cage.append(animal)
        logger.get_logger().info(f"Added animal to animal cage")
        return self

    def __sub__(self, animal):
        """
        Function to remove an animal from the animals_in_cage
        :param animal: Animal to remove from the animals_in_cage
        """
        if animal in self.animals_in_cage:
            self.animals_in_cage.remove(animal)
            logger.get_logger().info(f"removed animal from cage")

        logger.get_logger().info(f"failed to remove animal from cage")
        return self

    def __len__(self):
        """
        Function to return the amount of animals in the animals_in_cage
        :return: Amount of animals in the animals_in_cage
        """
        return len(self.animals_in_cage)

    def get_cage(self) -> list[Animal]:
        """
        Function to return the animal cage
        :return: Animals in the animal cage
        """
        return self.animals_in_cage

    def add_cage_to_cage(self, cage):
        """
        Function to add an animal to the animals_in_cage
        :param cage: Cage to add to the animals_in_cage
        """
        for animal in cage.get_cage():
            self.animals_in_cage.append(animal)


    def __str__(self):
        """
        Display the animals in the animals_in_cage for the user
        """
        if not self.animals_in_cage:
            return "Animal cage is empty"
        animal_strs = [str(animal) for animal in self.animals_in_cage]
        return f"AnimalCage with {len(self.animals_in_cage)} animals:\n" + "\n".join(animal_strs)

    def __repr__(self):
        """
        Function to print animals to developer
        """
        return f"AnimalCage(animals_in_cage={self.animals_in_cage!r})"
