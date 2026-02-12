import importlib.util
import sys
from pathlib import Path


class ModuleLoader:
    @staticmethod
    def find_class_name(path_to_module):
        """
        Function turns class path to class name
        :param path_to_module: Path to module
        :return: Class name
        """
        class_name = Path(path_to_module).stem.capitalize()
        return class_name

    @staticmethod
    def load_module(path_to_module, module_name=None):
        """
        Function gets path to module and loads it
        :param path_to_module: Path to module
        :param module_name: Module name
        :return: created module
        """
        if module_name is None:
            module_name = ModuleLoader.find_class_name(path_to_module)

        spec = importlib.util.spec_from_file_location(module_name, path_to_module)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module
