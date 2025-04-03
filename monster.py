import random
from character import Character
from hero import Hero

class Monster(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f" A wild Monster {self.name} appears!")

    def monster_attacks(self, hero):
        """Monster attacks the hero."""
        if hero.health_points > 0:
            damage = random.randint(1, 10)
            print(f" {self.name} attacks and deals {damage} damage!")
            hero.health_points = max(0, hero.health_points - damage)

    def drop_loot(self, hero):
        """Drop HP, a chance for a potion, and some gold."""
        health_points_collected = 10
        health_potion_collected = random.choice([True, False, False, True])
        gold_dropped = random.randint(5, 20)

        if health_potion_collected and hero.potions < 5:
            hero.potions += 1
            print(f" {self.name} dropped a Health Potion!")

        hero.health_points = min(hero.health_points + health_points_collected, 100)
        hero.gold += gold_dropped

        print(f" {self.name} is defeated! Hero gains {health_points_collected} HP.")
        print(f"  {self.name} dropped {gold_dropped} gold! Hero now has {hero.gold} gold.")
        print(f" Potions: {hero.potions} |  HP: {hero.health_points}")

        print(f"DEBUG: Monster drop potion: {health_potion_collected}")
