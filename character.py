import random

# Base class representing any character (Hero or Monster)
class Character:
    def __init__(self, name):
        self.name = name
        self._combat_strength = random.randint(5, 20)
        self._health_points = random.randint(50, 100)

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Combat strength must be a non-negative integer.")
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if not isinstance(value, int):
            raise ValueError("Health points must be an integer.")
        self._health_points = max(0, value)  # Ensure HP never goes below 0

    def __del__(self):
        print(f"A {self.__class__.__name__} object is being destroyed by the garbage collector.")