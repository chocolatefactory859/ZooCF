from abc import ABC
from random import randint

from logging_config import Logger

logger = Logger()


class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str = name
        self.sound: str = sound
        self.age: int = 201

        logger.info(f"Initialized animal: {self.name}")

    def __str__(self) -> str:
        return f"Name: {self.name} Sound: {self.sound} Age: {self.age}"

    def print_your_name(self) -> None:
        """
        Prints animal name
        """
        print(self.name)
        logger.debug("print_your_name called for %s", self.name)

    def print_your_sound(self) -> None:
        """
        Prints animal sound
        """
        print(self.sound)
        logger.debug("print_your_sound called for %s", self.name)

    def poop(self) -> None:
        """
        Prints poop
        """
        print("poop")
        logger.debug("%s performed poop()", self.name)
