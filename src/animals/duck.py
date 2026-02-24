from src.animals.animal import Animal


class Duck(Animal):
    def __init__(self, name: str):
        super().__init__(name, "Quack")
