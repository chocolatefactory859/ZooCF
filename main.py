from src.animal_factory import AnimalCreator
from src.file_handler import FileHandler
from src.parser import Parser


def call_animal_method(animal):
    """
    Calls animal methods
    :param animal: animal to call methods for
    """
    animal_class = getattr(animal, animal.__name__)
    animal_instance = animal_class()
    animal_instance.print_your_name()
    animal_instance.print_your_sound()

def main():
    """
    Gets file with animal names and performs
    actions on them
    :Raises: File not found error
    """
    argument_parser = Parser()
    animals_file_path = argument_parser.parse_input().get("filename")

    potential_animal_names = FileHandler.file_to_list(animals_file_path)

    for potential_animal_name in potential_animal_names:
        call_animal_method(AnimalCreator.animal_factory(potential_animal_name))


if __name__ == "__main__":
    main()
