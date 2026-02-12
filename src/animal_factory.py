import os

from src.module_loader import ModuleLoader


class AnimalCreator:
    @staticmethod
    def animal_factory(animal_name):
        """
        Creates animal from animal name
        :param animal_name: animal to create
        :raises: error if animal name does not exist
        :return: the created animal module
        """
        animal = os.environ.get(animal_name.upper())
        return ModuleLoader.load_module(animal)
