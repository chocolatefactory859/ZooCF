class AnimalAgeValueError(Exception):
    def __init__(self, message="Impossible value for animal age"):
        """
        Exception raised for impossible animal age
        param: animal_age: Received animal age
        param: message: Message to present on error
        """
        self.message = message

        super().__init__(self.message)
