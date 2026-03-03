from abc import ABC
from random import randint

from logging_config import Logger

logger = Logger()


def age_checker(func) -> None:
    """
    Wrapper for function, retries it until
    ValueError is not raised
    :param func: function to perform on
    :return: None
    """
    def wrapper(self, *args, **kwargs) -> None:
        while True:
            try:
                func(self, *args, **kwargs)
                return
            except ValueError:
                logger.debug("Retrying Animal initialization")
    return wrapper


class Animal(ABC):
    @age_checker
    def __init__(self, name: str, sound: str) -> None:
        self.name: str = name
        self.sound: str = sound
        self.age = randint(1, 200)

        if self.age > 100:
            raise ValueError("Age too high")

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

    def age_checker(self):
        self.__init__()
        while self.age > 100:
            self.__init__
        return self


