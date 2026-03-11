from objects.object_instance_factory import ObjectInstanceFactory


class AnimalGenerator:
    @staticmethod
    def generate_animals(file_path: str):
        """
        Load animals from file, creates them using
        the Object Factory
        param: file_path: File to get animal names from
        """
        with open(file_path) as f:
            for name in f.read().split():
                yield ObjectInstanceFactory.create_object(name, name)
