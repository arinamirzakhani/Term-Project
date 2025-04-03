import random
from character import Character

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health_points = 100  # Max HP
        self.potions = 0  # Start with 0 potions
        self.gold = 50  # Currency
        self.belt = []  # Inventory list

    def hero_attacks(self, monster):
        """Hero attacks the monster."""
        if monster.health_points > 0:
            damage = random.randint(1, 10)
            print(f"🗡 {self.name} attacks and deals {damage} damage!")
            monster.health_points = max(0, monster.health_points - damage)

    def use_health_potion(self):
        """Use a health potion to restore HP, but not beyond 100."""
        potions = [item for item in self.belt if item == "Health Potion"]  # List comprehension
        if potions:
            restored_health = min(100 - self.health_points, 20)
            self.health_points += restored_health
            self.potions -= 1
            self.belt.remove("Health Potion")  # Remove potion from inventory
            print(f" {self.name} used a health potion and restored {restored_health} HP! (Current HP: {self.health_points})")
        else:
            print(f" {self.name} has no potions left!")

    def buy_health_potion(self, merchant):
        """Buy a health potion from the merchant if available."""
        potion_price = 10

        if self.potions >= 5:
            print(f" {self.name} cannot carry more than 5 potions!")
            return

        if merchant.potion_stock > 0 and self.gold >= potion_price:
            self.gold -= potion_price
            self.potions += 1
            self.belt.append("Health Potion")  # Add potion to inventory
            merchant.potion_stock -= 1
            print(f"🛒 {self.name} bought a Health Potion from {merchant.name}! (Potions: {self.potions})")
        else:
            print(f" Not enough gold or stock available!")

    def check_and_use_potion(self):
        """Check if the hero has potions and use one if necessary (with nested conditionals)."""
        use_potion = input("🧪 Do you want to use a health potion? (y/n): ").strip().lower()
        if use_potion == "y":
            potions = [item for item in self.belt if item == "Health Potion"]  # List comprehension
            if potions:
                self.use_health_potion()
            else:
                print(" You chose to use a potion, but you don't have any!")
