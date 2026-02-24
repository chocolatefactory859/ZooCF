from src.animals.animal import Animal
from src.input.text_file_reader import TextFileReader
from src.objects.object_instance_creator import ObjectInstanceCreator
from src.parser.zoo_parser import ZooParser


def main():
    argument_parser = ZooParser()
    received_input = argument_parser.parse_input()
    animals_file_path = received_input.get("filepath")

    potential_animal_names = TextFileReader.read_input_to_words(animals_file_path)

    for potential_animal_name in potential_animal_names:
        animal: Animal = ObjectInstanceCreator.create_object(potential_animal_name, potential_animal_name)
        animal.print_your_name()
        animal.print_your_sound()
        print(f"Animal type: {type(animal)}")
        animal.poop()


if __name__ == "__main__":
    main()
