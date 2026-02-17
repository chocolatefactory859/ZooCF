from src.animal import Animal
from src.animal_factory import ObjectCreator
from src.input.file_handler import TextFileHandler
from src.parser.argument_input_parser import ZooParser


def call_animal_method(animal: Animal) -> None:
    """
    Calls animal methods
    Param: animal: animal to call methods for
    """
    animal.print_your_name()
    animal.print_your_sound()

def main():
    """
    Gets file with animal names and performs
    actions on them
    Raise: File not found error
    """
    try:
        argument_parser = ZooParser()
        animals_file_path = argument_parser.parse_input().get("filename")

        potential_animal_names = TextFileHandler.read_input(animals_file_path)

        for potential_animal_name in potential_animal_names:
            animal_to_call = ObjectCreator.create_object(potential_animal_name)
            call_animal_method(animal_to_call)
    except Exception as error:
        print(f"An error has occurred: {error}")


if __name__ == "__main__":
    main()
