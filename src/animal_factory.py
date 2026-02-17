import os
from types import ModuleType

from src.module_loader import ModuleLoader


class ObjectCreator:
    @staticmethod
    def create_object(object_name: str) -> ModuleType:
        """
        Creates animal from animal name
        Param: animal_name: animal to create
        Return: the created animal instance
        Raise: error if animal name does not exist
        """
        try:
            object = os.getenv("LOCAL_PATH") + os.getenv(object_name.upper())
            object_module = ModuleLoader.load_module(object)
            object_class = getattr(object_module, object_module.__name__)
            animal_instance = object_class()
            return animal_instance
        except ModuleNotFoundError as error:
            raise ModuleNotFoundError(f"Module {object_name} not found: {error}")
