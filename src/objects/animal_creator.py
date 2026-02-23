import os
from types import ModuleType

from src.modules.module_loader import ModuleLoader


class CreateAnimal:
    @staticmethod
    def create_animal(animal_name: str) -> ModuleType:
        """
        Function gets animal name, and searches for it in dict
        Then, creates animal instance
        :param animal_name:
        :return:
        """
        animal_to_create = None
        animals_to_get_names = os.getenv("ANIMALS_WITH_SPECIAL_NAMES").split()
        animals = {}
        for animal_to_get_name in animals_to_get_names:
            animals[animal_to_get_name] = os.getenv(animal_to_get_name+ "_NAMES")


        if (animal_name.upper() in animals):
            animal_to_create = animal_name

        if(animal_to_create is None):
            animal_to_create = next((key for key, value in animals.items() if animal_name in value), None)

        object_to_create = os.getenv(animal_to_create.upper())
        object_module = ModuleLoader.load_module(object_to_create)

        object_class = getattr(object_module, object_module.__name__)
        object_instance = object_class(animal_name)

        return object_instance
