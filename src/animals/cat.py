from src.animal import Animal


class Cat(Animal):
    def __iter__(self):
        """
        Function adds iter functionality to class
        """
        yield self

    def print_your_name(self):
        """
        Function prints animal name
        """
        print("Cat")

    def print_your_sound(self):
        """
        Function prints animal sound
        """
        print("Meow")
