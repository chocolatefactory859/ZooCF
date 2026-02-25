from abc import ABC

from logging_config import logger


class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str= name
        self.sound: str = sound
        logger.get_logger().info(f"initializing animal: {self.name}")

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

    def __str__(self):
        return f"Animal: {self.name} sound: {self.sound}"
