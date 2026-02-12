import importlib.util
import sys
from pathlib import Path


class ModuleLoader:
    @staticmethod
    def find_class_name(path_to_module):
        class_name = Path(path_to_module).stem.capitalize()
        return class_name

    @staticmethod
    def load_module(path_to_module, module_name=None):
        if module_name is None:
            module_name = ModuleLoader.find_class_name(path_to_module)

        spec = importlib.util.spec_from_file_location(module_name, path_to_module)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module

