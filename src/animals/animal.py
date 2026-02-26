from abc import ABC

from logging_config import Logger

logger = Logger()

class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str= name
        self.sound: str = sound
        logger.get_logger().info(f"initialized animal: {self.name}")

    def __str__(self):
        return f"Animal: {self.name} sound: {self.sound}"

    def print_your_name(self):
        """
        Function prints animal name
        """
        print(self.name)
        logger.get_logger().info(f"printed animal name: {self.name}")

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        print(self.sound)
        logger.get_logger().info(f"printed animal sound: {self.sound}")

    def poop(self):
        """
        Function prints poop
        """
        print("poop")
        logger.get_logger().info(f"printed animal poop: {self.name}")
