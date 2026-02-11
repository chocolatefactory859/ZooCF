import os
from src.animals.cat import Cat
from src.animals.dog import Dog
from src.animals.duck import Duck


os.environ["ANIMALS"] = {"cat":Cat, "dog": Dog, "duck": Duck}
