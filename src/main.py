import sys

from animals.animal import Animal
from animals.cage.animal_cage import AnimalCage
from input.text_file_reader import TextFileReader
from logging_config import Logger
from objects.object_instance_creator import ObjectInstanceCreator
from parser.zoo_parser import ZooParser

from logging_config import logger

def main():

    logger.get_logger().info("starting main")

    argument_parser = ZooParser()
    received_input = argument_parser.parse_input()
    animals_file_path = received_input.get("filepath")

    potential_animal_names = TextFileReader.read_input_to_words(animals_file_path)
    animal_cage = AnimalCage()

    for potential_animal_name in potential_animal_names:
        animal: Animal = ObjectInstanceCreator.create_object(potential_animal_name, potential_animal_name)
        #zoo2:
        #animal.print_your_name()
        #animal.print_your_sound()
        #logger.info(f"Animal type: {type(animal)}")
        #animal.poop()
        animal_cage.add_animal(animal)

    animal_cage.print_animals_to_user()
    animal_cage.remove_animal(animal)
    animal_cage.print_animals_to_user()



if __name__ == "__main__":
    main()
