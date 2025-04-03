import random
from character import Character
from hero import Hero

class Monster(Character):
    def __init__(self, name, health=None, attack=None):
        # Randomized health and attack if not provided (dynamic spawning)
        self.health_points = health if health is not None else random.randint(20, 50)
        self.attack_power = attack if attack is not None else random.randint(5, 15)
        super().__init__(name)
        self.behavior = "Neutral"  # Default behavior
        print(f"A wild {self.name} appears! | HP: {self.health_points} | ATK: {self.attack_power}")

    def monster_attacks(self, hero):
        """Monster attacks the hero."""
        if hero.health_points > 0:
            damage = random.randint(1, self.attack_power)
            print(f"{self.name} attacks and deals {damage} damage!")
            hero.health_points = max(0, hero.health_points - damage)

    def drop_loot(self, hero):
        """Drop HP, a chance for a potion, and some gold."""
        health_points_collected = 10
        health_potion_collected = random.choice([True, False, False, True])
        gold_dropped = random.randint(5, 20)

        if health_potion_collected and hero.potions < 5:
            hero.potions += 1
            print(f"{self.name} dropped a Health Potion!")

        hero.health_points = min(hero.health_points + health_points_collected, 100)
        hero.gold += gold_dropped

        print(f"{self.name} is defeated! Hero gains {health_points_collected} HP.")
        print(f"{self.name} dropped {gold_dropped} gold! Hero now has {hero.gold} gold.")
        print(f"Potions: {hero.potions} | HP: {hero.health_points}")
        print(f"DEBUG: Monster drop potion: {health_potion_collected}")
