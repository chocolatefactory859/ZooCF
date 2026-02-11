from src.animal import Animal


class Cat(Animal):
    def __iter__(self):
        yield self
    def print_your_name(self):
        """
        prints animal name
        :return: none
        """
        print("Cat")

    def print_your_sound(self):
        """
        prints animal sound
        :return: none
        """
        print("Meow")

