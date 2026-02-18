from src.animals.animal import Animal


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "How")
