from animals.animal import Animal


class AnimalCage:
    def __init__(self):
        self.animal_cage: list[Animal] = []

    def __add__(self, animal):
        """
        Function to add an animal to the animal_cage
        :param animal: Animal to add to the animal_cage
        """
        self.animal_cage.append(animal)
        return self

    def __sub__(self, animal):
        """
        Function to remove an animal from the animal_cage
        :param animal: Animal to remove from the animal_cage
        """
        if animal in self.animal_cage:
            self.animal_cage.remove(animal)
        return self

    def get_cage(self) -> list[Animal]:
        """
        Function to return the animal cage
        :return:
        """
        return self.animal_cage

    def amount_of_animals(self):
        """
        Function to return the amount of animals in the animal_cage
        :return: Amount of animals in the animal_cage
        """
        return len(self.animal_cage)

    def add_cage_to_cage(self, cage):
        """
        Function to add an animal to the animal_cage
        :param cage: Cage to add to the animal_cage
        """
        for animal in cage.get_cage():
            self.animal_cage.append(animal)

    def print_animals_to_user(self):
        """
        Display the animals in the animal_cage for the user
        """
        print("Animals in the animal cage:")
        for animal in self.animal_cage:
            print(animal)

    def print_animals_to_developer(self):
        """
        Function to print animals to developer
        """
        for animal in self.animal_cage:
            print(animal)
