import random
from character import Character
from monster import Monster

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Hero {self.name} has entered the battle!")

    def hero_attacks(self, monster):
        try:
            if not isinstance(monster, Monster):
                raise TypeError("The target must be a Monster instance.")
            if not isinstance(monster.health_points, int):
                raise ValueError("Monster's health points must be an integer.")

            if monster.health_points > 0:
                damage = random.randint(1, 10)
                print(f"Hero {self.name} attacks and deals {damage} damage!")
                monster.health_points = max(0, monster.health_points - damage)
        except Exception as e:
            print(f"Error in hero_attacks: {e}")

    def __del__(self):
        print(f"The Hero {self.name} object is being destroyed by the garbage collector.")
        super().__del__()
