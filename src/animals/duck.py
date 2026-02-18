from src.animals.animal import Animal


class Duck(Animal):
    def __init__(self):
        super().__init__("Duck", "Quack")
