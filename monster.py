import random
from character import Character
from hero import Hero

class Monster(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"A wild Monster {self.name} appears!")

    def monster_attacks(self, hero):


        if not isinstance(hero, Hero):
            raise TypeError("The target must be a Hero instance.")
        if not isinstance(hero.health_points, int):
            raise ValueError("Hero's health points must be an integer.")


        if hero.health_points > 0:
            try:
                damage = random.randint(1, 10)
                print(f"Monster {self.name} attacks and deals {damage} damage!")
                hero.health_points = max(0, hero.health_points - damage)  # Prevent negative HP
            except Exception as e:
                print(f"Error in monster_attacks: {e}")

    def __del__(self):

        print(f"The Monster {self.name} object is being destroyed by the garbage collector.")
        super().__del__()
