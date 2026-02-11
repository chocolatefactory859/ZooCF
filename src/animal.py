from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def print_your_name(self):
        """
        prints animal name
        :return: none
        """
        pass

    @abstractmethod
    def print_your_sound(self):
        """
        prints animal sound
        :return: none
        """
        pass
