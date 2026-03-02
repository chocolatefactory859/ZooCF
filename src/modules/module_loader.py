import importlib
from types import ModuleType


class ModuleLoader:
    @staticmethod
    def find_class_name(path_to_module: str) -> str:
        """
        Function turns class path to class name
        Param: path_to_module: Path to module
        Return: Class name
        """
        parts = path_to_module.split(".")
        class_name = parts[-1]
        return class_name.capitalize()

    @staticmethod
    def load_module(path_to_module: str) -> ModuleType:
        """
        Function gets path to module and loads it
        Param: path_to_module: Path to module
        Return: created module
        """
        module = importlib.import_module(path_to_module)
        module.__name__ = ModuleLoader.find_class_name(path_to_module)

        return module
