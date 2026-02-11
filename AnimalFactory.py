from Animal import Animal
from Animals.Cat import Cat
from Animals.Dog import Dog
from Animals.Duck import Duck


def animal_factory(animal_name):
    """
    creates animal
    :param animal_name: animal to create
    :raises: error if animal name does not exist
    :return: the created animal
    """
    animals = {
        'cat': Cat,
        'dog': Dog,
        'duck': Duck,
    }

    try:
        return animals[animal_name]()
    except KeyError:
        raise ValueError(f"Unknown animal type: {animal_name}")
