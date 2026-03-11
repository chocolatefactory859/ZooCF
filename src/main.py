from animals.cage.animal_cage import AnimalCage
from generator.animal_generator import AnimalGenerator
from generator.animal_generator2 import AnimalGenerator2
from parser.zoo_parser import ZooParser

from logging_config import Logger
from toilet.toilet import Toilet
from toilet.toilet2 import Toilet2

logger = Logger()


def main():
    logger.info("Starting zoo")

    argument_parser = ZooParser()
    received_input = argument_parser.parse_input()
    animals_file_path = received_input.get("filepath")
    toilet_output_path = received_input.get("toilet_output")

    animal_cage = AnimalCage()
    animal_cage_2 = AnimalCage()

    animal_generator = AnimalGenerator2(animals_file_path)

    for animal in animal_generator:
        animal.print_your_name()
        animal.print_your_sound()
        animal.poop()

        animal_cage = animal_cage + animal
        animal_cage_2 = animal_cage_2 + animal

    print(animal_cage)
    animal_cage -= animal

    with Toilet2.toilet_context(toilet_output_path) as toilet:
        print(animal_cage)
        toilet.flush_toilet()
        print(f"Amount of animals in cage: {len(animal_cage)}")

    animal_cage += animal_cage_2
    print(animal_cage)


if __name__ == "__main__":
    main()
