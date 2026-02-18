from src.objects.object_factory import ObjectInstanceCreator
from src.input.text_file_reader import TextFileReader
from src.parser.zoo_parser import ZooParser


def main():
    argument_parser = ZooParser()
    recieved_input = argument_parser.parse_to_words()
    animals_file_path = recieved_input.get("filepath")

    potential_animal_names = TextFileReader.read_input(animals_file_path)

    for potential_animal_name in potential_animal_names:
        animal_to_call = ObjectInstanceCreator.create_object(potential_animal_name)
        animal_to_call.print_your_name()
        animal_to_call.print_your_sound()

if __name__ == "__main__":
    main()
