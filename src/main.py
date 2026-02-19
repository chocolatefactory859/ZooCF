from src.objects.object_factory import ObjectInstanceCreator
from src.input.text_file_reader import TextFileReader
from src.parser.zoo_parser import ZooParser


def main():
    argument_parser = ZooParser()
    received_input = argument_parser.parse_input()
    animals_file_path = received_input.get("filepath")

    potential_animal_names = TextFileReader.parse_input_to_word(animals_file_path)

    for potential_animal_name in potential_animal_names:
        animal = ObjectInstanceCreator.create_object(potential_animal_name)
        animal.print_your_name()
        animal.print_your_sound()


if __name__ == "__main__":
    main()
