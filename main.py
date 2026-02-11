from src import parser
import sys

from src.animal_factory import AnimalCreator
from src.file_handler import FileHandler
from src.parser import Parser
from src.zoo import Zoo


def main():
    """
    gets file with animal names and performs
    actions on them
    :raises: file not found error
    :return: none
    """

    # parse input from user
    argument_parser = Parser()
    argument_parser.__init__()
    animals_file_path = argument_parser.parse_input().get("filename")

    # get potential animal names
    potential_animal_names = FileHandler.file_to_list(animals_file_path)

    # create animals
    animals = Zoo.create_animals(potential_animal_names)

    # call animal methods
    Zoo.call_animal_methods(animals)



if __name__ == "__main__":
    main()
    