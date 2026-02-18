import importlib.util, sys
from pathlib import Path
from types import ModuleType


class ModuleLoader:
    @staticmethod
    def find_class_name(path_to_module: str) -> str:
        """
        Function turns class path to class name
        Param: path_to_module: Path to module
        Return: Class name
        """
        class_name = Path(path_to_module).stem.capitalize()
        return class_name

    @staticmethod
    def load_module(path_to_module: str, module_name=None) -> ModuleType:
        """
        Function gets path to module and loads it
        Param: path_to_module: Path to module
        Param: module_name: Module name
        Return: created module
        Raise: ModuleNotFound error
        """
        if module_name is None:
            module_name = ModuleLoader.find_class_name(path_to_module)

        try:
            specifier = importlib.util.spec_from_file_location(module_name, path_to_module)
            module = importlib.util.module_from_spec(specifier)
            sys.modules[module_name] = module
            specifier.loader.exec_module(module)
            return module

        except ModuleNotFoundError as error:
            print(f"Error: {error}")
