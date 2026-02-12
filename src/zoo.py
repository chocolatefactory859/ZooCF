from src.animal_factory import AnimalCreator


class Zoo:
    @staticmethod
    def call_animal_method(animal):
        """
        Calls animal methods
        :param animal: animal to call methods for
        """
        animal_class = getattr(animal, animal.__name__)
        animal_instance = animal_class()
        animal_instance.print_your_name()
        animal_instance.print_your_sound()
