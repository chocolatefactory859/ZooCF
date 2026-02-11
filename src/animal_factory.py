from src.animals.cat import Cat
from src.animals.dog import Dog
from src.animals.duck import Duck


class AnimalCreator:
    def animal_factory(self, animal_name):
        """
        creates animal
        :param animal_name: animal to create
        :raises: error if animal name does not exist
        :return: the created animal
        """
        animals = {
            'cat': Cat,
            'dog': Dog,
            'duck': Duck,
        }

        try:
            return animals[animal_name.lower()]()
        except KeyError:
            raise ValueError(f"Unknown animal type: {animal_name}")
