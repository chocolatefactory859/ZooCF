from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def print_your_name(self):
        """
        Function prints animal name
        """
        pass

    @abstractmethod
    def print_your_sound(self):
        """
        Function prints animal sound
        """
        pass
