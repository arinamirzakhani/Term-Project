class Merchant:
    def __init__(self, name):
        self.name = name
        self.items_for_sale = ["Leather Boots", "Magic Ring"]
        self.potion_stock = 3  # Merchant starts with 3 potions

    def sell_health_potion(self, hero):
        """Sell health potions to the hero."""
        potion_price = 10

        if self.potion_stock == 0:
            print(f" {self.name} has no more potions left!")
            return

        if hero.potions >= 5:
            print(f"⚠ {hero.name} already has the maximum number of potions (5)!")
            return


        print(f" {hero.name}, you currently have {hero.gold} gold.")
        print(f" {self.name} offers Health Potions for {potion_price} gold each.")
        buy = input(" Do you want to proceed with the purchase? (y/n): ").strip().lower()

        if buy == "y":
            if hero.gold >= potion_price:
                hero.gold -= potion_price
                hero.potions += 1
                hero.belt.append("Health Potion")
                self.potion_stock -= 1


                healed_amount = min(15, 100 - hero.health_points)
                hero.health_points += healed_amount

                print(f" {hero.name} bought a Health Potion!  (Potions: {hero.potions}, Gold left: {hero.gold})")
                print(f" {hero.name} also regained {healed_amount} HP! (Current HP: {hero.health_points})")
