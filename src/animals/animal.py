import os
from abc import ABC
from random import randint

from animals.animal_exceptions import AnimalAgeValueError
from decorators.retry import retry_until_success
from logging_config import Logger

logger = Logger()
MAX_ANIMAL_AGE = int(os.getenv("MAX_ANIMAL_AGE"))


def randomize_age():
    """
    Randomizes age from 1 - 200
    """
    return randint(1, 200)


class Animal(ABC):
    @retry_until_success(exception_to_catch=AnimalAgeValueError)
    def __init__(self, name: str, sound: str) -> None:
        self.name: str = name
        self.sound: str = sound
        self.age = randomize_age()

        if self.age > MAX_ANIMAL_AGE:
            raise AnimalAgeValueError()

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
