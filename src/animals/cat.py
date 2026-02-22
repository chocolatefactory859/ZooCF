from src.animals.animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__(self.__class__.__name__, "Meow")
