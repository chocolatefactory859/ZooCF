from src.animal import Animal
from src.object_factory import ObjectCreator
from src.input.text_file_handler import TextFileHandler
from src.parser.zoo_parser import ZooParser


def main():
    argument_parser = ZooParser()
    recieved_input = argument_parser.parse_to_words()
    animals_file_path = recieved_input.get("filepath")

    potential_animal_names = TextFileHandler.read_input(animals_file_path)

    for potential_animal_name in potential_animal_names:
        animal_to_call = ObjectCreator.create_object(potential_animal_name)
        animal_to_call.print_your_name()
        animal_to_call.print_your_sound()

if __name__ == "__main__":
    main()
