import os
from types import ModuleType

from src.module_loader import ModuleLoader


class AnimalCreator:
    @staticmethod
    def animal_factory(animal_name: str) -> ModuleType:
        """
        Creates animal from animal name
        Param: animal_name: animal to create
        Return: the created animal instance
        Raise: error if animal name does not exist
        """
        animal = os.getenv(animal_name.upper())
        animal_module = ModuleLoader.load_module(animal)
        animal_class = getattr(animal_module, animal_module.__name__)
        animal_instance = animal_class()
        return animal_instance
