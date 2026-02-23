from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def print_your_name(self):
        """
        Function prints animal name
        """
        print(self.name)

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        print(self.sound)

    def poop(self):
        """
        Function prints poop
        """
        print("poop")
