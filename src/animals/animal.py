from abc import ABC
import logging

class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str= name
        self.sound: str = sound

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

    def to_string(self):
        return (f"Animal: {self.name}, Sound: {self.sound}")
