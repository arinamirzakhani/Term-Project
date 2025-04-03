import random
import pickle
from hero import Hero
from monster import Monster
from merchant import Merchant

# Function to save the game state to a file
def save_game(hero):
    with open('hero_save.pkl', 'wb') as file:
        pickle.dump(hero, file)
    print("Game saved successfully!")

# Function to save hero's health points to a file
def save_hero_health(hero):
    with open('hero_health.txt', 'w') as file:
        file.write(f"Hero {hero.name}'s current health: {hero.health_points}")
    print(f"Hero's health saved in hero_health.txt.")

# Function to load the game state from a file
def load_game():
    try:
        with open('hero_save.pkl', 'rb') as file:
            hero = pickle.load(file)
        print(f"Game loaded. Welcome back, Hero {hero.name}!")
        return hero
    except FileNotFoundError:
        print("No saved game found.")
        return None

# Main function
def main():
    # Load the saved game or create a new hero
    hero = load_game()
    if hero is None:
        hero_name = input("Enter your Hero's name: ")
        hero = Hero(hero_name)

    # Monster creation
    monster = Monster("Goblin")

    # Start combat
    while hero.health_points > 0 and monster.health_points > 0:
        print("\n--- Combat Begins ---")
        hero.hero_attacks(monster)
        if monster.health_points <= 0:
            print(f"{monster.name} is dead!")
            monster.drop_loot(hero)  # Drop loot (including gold) when the monster is defeated
            break

        monster.monster_attacks(hero)
        if hero.health_points <= 0:
            print(f"{hero.name} is dead!")
            break

        # Display the hero's current health and gold
        print(f"Hero {hero.name} current health: {hero.health_points} and {hero.gold} gold.")

        # Check if the hero's health is low and prompt for a health potion
        if hero.health_points < 20:  # Adjust the threshold (20) as needed
            # Only prompt if the hero has potions left
            if hero.potions > 0:
                use_potion = input("Your health is low! Do you want to use a health potion? (y/n): ").strip().lower()
                if use_potion == "y":
                    hero.use_health_potion()  # Use the potion if the user chooses "y"
                    print(f" Hero's health after using potion: {hero.health_points}")
                else:
                    print("You chose not to use a health potion.")
            else:
                print("You have no health potions left.")

        # After checking health, ask again if health drops to 0
        if hero.health_points == 0:
            print("You are out of health points! Game Over!")
            break

    # After combat, save the game
    save_game(hero)  # Example data, you can adjust it as needed

# Run the game
if __name__ == "__main__":
    main()