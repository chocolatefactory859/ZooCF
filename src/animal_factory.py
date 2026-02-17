import os
from types import ModuleType

from src.module_loader import ModuleLoader


class AnimalCreator:
    @staticmethod
    def animal_factory(animal_name: str) -> ModuleType:
        """
        Creates animal from animal name
        :param animal_name: animal to create
        :raises: error if animal name does not exist
        :return: the created animal instance
        """
        animal = os.getenv(animal_name.upper())
        animal_module = ModuleLoader.load_module(animal)
        animal_class = getattr(animal_module, animal_module.__name__)
        animal_instance = animal_class()
        return animal_instance

