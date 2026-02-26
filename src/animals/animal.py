from abc import ABC

from logging_config import Logger


class Animal(ABC):
    def __init__(self, name: str, sound: str) -> None:
        self.name: str= name
        self.sound: str = sound
        self.logger = Logger()
        self.logger.get_logger().info(f"initialized animal: {self.name}")

    def __str__(self):
        return f"Animal: {self.name} sound: {self.sound}"

    def print_your_name(self):
        """
        Function prints animal name
        """
        print(self.name)
        self.logger.get_logger().info(f"printed animal name: {self.name}")

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        print(self.sound)
        self.logger.get_logger().info(f"printed animal sound: {self.sound}")

    def poop(self):
        """
        Function prints poop
        """
        print("poop")
        self.logger.get_logger().info(f"printed animal poop: {self.name}")
