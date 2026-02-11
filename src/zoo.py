from src.animal_factory import AnimalCreator


class Zoo:
    @staticmethod
    def create_animals(animal_names):
        # gets input from user and returns list of animal instances
        # first, create all animals

        animals = []

        for animal_name in animal_names:
            animal_creator = AnimalCreator()
            animals += animal_creator.animal_factory(animal_name)

        return animals

    @staticmethod
    def call_animal_methods(animals):
        for animal in animals:
            animal.print_your_name()
            animal.print_your_sound()
