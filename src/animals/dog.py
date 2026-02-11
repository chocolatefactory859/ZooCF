from src.animal import Animal


class Dog(Animal):
    def __iter__(self):
        yield self
    def print_your_name(self):
        """
        prints animal name
        :return: none
        """
        print("Dog")

    def print_your_sound(self):
        """
        prints animal sound
        :return: none
        """
        print("How")
