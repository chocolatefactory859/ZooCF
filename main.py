from AnimalFactory import animal_factory
import sys


def main():
    """
    gets file with animal names and performs
    actions on them
    :raises: file not found error
    :return: none
    """
    animals_file_path = sys.argv[1]
    try:
        with open(animals_file_path, 'r') as file:
            for line in file:
                potential_animal_names = line.split()
                for potential_animal_name in potential_animal_names:
                    animal = animal_factory(potential_animal_name)
                    animal.print_your_sound()
                    animal.print_your_name()
    except FileNotFoundError:
        raise FileNotFoundError(f"Unknown file: {animals_file_path}")


if __name__ == "__main__":
    main()
    