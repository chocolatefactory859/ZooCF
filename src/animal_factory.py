import json
import os
import sys

from src import module_loader
from src.animals.cat import Cat
from src.animals.dog import Dog
from src.animals.duck import Duck

import importlib.util

from src.module_loader import ModuleLoader


class AnimalCreator:
    @staticmethod
    def animal_factory(animal_name):
        """
        creates animal
        :param animal_name: animal to create
        :raises: error if animal name does not exist
        :return: the created animal
        """
        animal = os.environ.get(animal_name.upper())


        return ModuleLoader.load_module(animal)
     #   if animals:
     #       animals_dict = json.loads(animals)

    #    try:
    #        return animals_dict[animal_name.lower()]()
    #    except KeyError:
    #        raise ValueError(f"Unknown animal type: {animal_name}")
