from src.animals.animal import Animal


class Duck(Animal):
    def __init__(self, name):
        super().__init__(name, "Quack")
