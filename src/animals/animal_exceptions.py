class AnimalAgeValueError(Exception):
    def __init__(self, message="Impossible value for animal age"):
        """
        Exception raised for impossible animal age
        :param animal_age: received animal age
        :param message: message to present on error
        """
        self.message = message

        super().__init__(self.message)
