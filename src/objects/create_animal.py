from types import ModuleType

from src.objects.object_instance_creator import ObjectInstanceCreator


class CreateAnimal:
    @staticmethod
    def create_animal(animal_name: str) -> ModuleType:
        """
        Function gets animal name, and searches for it in dict
        Then, creates animal instance
        :param animal_name:
        :return:
        """
        animals = {"CAT": ["cat1", "cat2"], "DOG": ["dog1", "dog2"], "DUCK": ["duck1", "duck2"]}

        if (animal_name.upper() in animals):
            return ObjectInstanceCreator.create_object(animal_name, animal_name)
        animal_to_create = next((key for key, value in animals.items() if animal_name in value), None)

        return ObjectInstanceCreator.create_object(animal_to_create, animal_name)
