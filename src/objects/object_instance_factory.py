import os
from types import ModuleType

from modules.module_loader import ModuleLoader


class ObjectInstanceFactory:
    @staticmethod
    def create_object(object_name: str, *args, **kwargs) -> ModuleType:
        """
        Creates object from object name
        Param: object_name: object to create
        Return: the created object instance
        Raise: error if object name does not exist
        """
        object_to_create = os.getenv(object_name.upper())
        object_module = ModuleLoader.load_module(object_to_create)

        object_class = getattr(object_module, object_module.__name__)
        object_instance = object_class(*args, **kwargs)

        return object_instance
