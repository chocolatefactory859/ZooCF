from objects.object_instance_factory import ObjectInstanceFactory


class AnimalGenerator:
    @staticmethod
    def generate_animals(file_path: str):
        """
        Load animals from file, creates them using
        the Object Factory
        param: file_path: File to get animal names from
        """
        with open(file_path) as file:
            for animal_name in file.read().split():
                yield ObjectInstanceFactory.create_object(animal_name, animal_name)

    @staticmethod
    def generate_animals2(file_path: str):
        """
        Load animals from file, creates them using
        the Object Factory
        param: file_path: File to get animal names from
        """
        with open(file_path) as file:
            return (ObjectInstanceFactory.create_object(animal_name, animal_name)
                    for animal_name in file.read().split())
