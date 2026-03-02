from abc import ABC

from logging_config import Logger

logger = Logger()

class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str = name
        self.sound: str = sound
        logger.info(f"Initialized animal: {self.name}")
        logger.debug("Animal created with name=%s, sound=%s", self.name, self.sound)

    def __str__(self):
        return f"Animal: {self.name} sound: {self.sound}"

    def print_your_name(self):
        """
        Function prints animal name
        """
        print(self.name)
        logger.debug("print_your_name called for %s", self.name)

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        print(self.sound)
        logger.debug("print_your_sound called for %s", self.name)

    def poop(self):
        """
        Function prints poop
        """
        print("poop")
        logger.debug("%s performed poop()", self.name)
