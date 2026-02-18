import os
from types import ModuleType

from src.modules.module_loader import ModuleLoader


LOCAL_PATH = os.getenv("LOCAL_PATH")

class ObjectInstanceCreator:
    @staticmethod
    def create_object(object_name: str) -> ModuleType:
        """
        Creates object from object name
        Param: object_name: object to create
        Return: the created object instance
        Raise: error if object name does not exist
        """
        object = LOCAL_PATH + os.getenv(object_name.upper())
        #object = os.getenv(object_name.upper())
        object_module = ModuleLoader.load_module(object)

        object_class = getattr(object_module, object_module.__name__)
        object_instance = object_class()

        return object_instance
