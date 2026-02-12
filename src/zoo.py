from src.animal_factory import AnimalCreator


class Zoo:
    @staticmethod
    def create_animals(animal_names):
        """
        Function turns given animal names into a
        list of animal instances
        :param animal_names: list pf animal names to turn into instances
        :return: list of animal instances
        """

        animals = []

        for animal_name in animal_names:
            animal_creator = AnimalCreator()
            animals += animal_creator.animal_factory(animal_name)

        return animals

    @staticmethod
    def call_animal_method(animal):
        animal_class = getattr(animal, animal.__name__)
        animal_instance = animal_class()
        animal_instance.print_your_name()
        animal_instance.print_your_sound()

    @staticmethod
    def call_animal_methods(animals):
        for animal in animals:
            Zoo.call_animal_method(animal)
