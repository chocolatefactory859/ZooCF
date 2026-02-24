from abc import ABC
import logging

class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str= name
        self.sound: str = sound
        self.logger = logging.getLogger(__name__)

    def print_your_name(self):
        """
        Function prints animal name
        """
        self.logger.info(self.name)

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        self.logger.info(self.sound)

    def poop(self):
        """
        Function prints poop
        """
        self.logger.info("poop")

    def to_string(self):
        return (f"Animal: {self.name}, Sound: {self.sound}")
