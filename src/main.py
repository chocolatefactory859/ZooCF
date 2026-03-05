import os

from animals.animal import Animal
from animals.cage.animal_cage import AnimalCage
from input.text_file_reader import TextFileReader
from objects.object_instance_factory import ObjectInstanceFactory
from parser.zoo_parser import ZooParser

from logging_config import Logger
from toilet.toilet import Toilet


logger = Logger()


def main():
    logger.info("Starting zoo")

    argument_parser = ZooParser()
    received_input = argument_parser.parse_input()
    animals_file_path = received_input.get("filepath")
    toilet_output_path = received_input.get("toilet_output")

    potential_animal_names = TextFileReader.read_input_to_words(animals_file_path)
    animal_cage = AnimalCage()
    animal_cage_2 = AnimalCage()

    for potential_animal_name in potential_animal_names:
        animal: Animal = ObjectInstanceFactory.create_object(potential_animal_name, potential_animal_name)
        #zoo2:
        animal.print_your_name()
        animal.print_your_sound()
        animal.poop()
        animal_cage = animal_cage + animal
        animal_cage_2 = animal_cage_2 + animal

    print(animal_cage)
    animal_cage -= animal

    with Toilet(toilet_output_path=toilet_output_path) as toilet:
        print(animal_cage)
        toilet.flush_toilet()
        print(f"Amount of animals in cage: {len(animal_cage)}")

    animal_cage += animal_cage_2
    print(animal_cage)


if __name__ == "__main__":
    main()
