import pickle
from hero import Hero
from monster import Monster



# Adaptive Enemy Spawner
def adaptive_enemy_spawn(hero):
    enemy_types = ["Goblin", "Orc", "Troll"]

    # Create enemies with random stats using list comprehension
    spawned_enemies = [
        Monster(name=enemy)
        for enemy in enemy_types
    ]

    # Assign behavior based on hero stats
    for enemy in spawned_enemies:
        if hero.level > 5:
            if hero.health_points < 30:
                enemy.behavior = "Defensive"
            else:
                enemy.behavior = "Aggressive"
        else:
            enemy.behavior = "Cowardly"

    return spawned_enemies


# Function to save the game state to a file
def save_game(hero):
    with open('hero_save.pkl', 'wb') as f:
        pickle.dump(hero, f)
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

    # Assign hero level
    hero.level = int(input("Enter Hero's Level (for testing adaptive spawning): "))

    # Spawn adaptive enemies
    enemies = adaptive_enemy_spawn(hero)

    # Display spawned enemies
    print("\n--- Enemies Spawned ---")
    for enemy in enemies:
        print(
            f"Name: {enemy.name} | HP: {enemy.health_points} | ATK: {enemy.attack_power} | Behavior: {enemy.behavior}")

    # Battle loop against each enemy
    for monster in enemies:
        print(f"\nA wild {monster.name} appears! Prepare to fight.")

        while hero.health_points > 0 and monster.health_points > 0:
            print("\n--- Combat Begins ---")
            hero.hero_attacks(monster)

            if monster.health_points <= 0:
                print(f"{monster.name} is dead!")
                monster.drop_loot(hero)
                break

            monster.monster_attacks(hero)

            if hero.health_points <= 0:
                print(f"{hero.name} is dead!")
                break

            print(f"Hero {hero.name} current health: {hero.health_points} and {hero.gold} gold.")

            if hero.health_points < 20:
                if hero.potions > 0:
                    use_potion = input(
                        "Your health is low! Do you want to use a health potion? (y/n): ").strip().lower()
                    if use_potion == "y":
                        hero.use_health_potion()
                        print(f"Hero's health after using potion: {hero.health_points}")
                    else:
                        print("You chose not to use a health potion.")
                else:
                    print("You have no health potions left.")

            if hero.health_points == 0:
                print("You are out of health points! Game Over!")
                break

        if hero.health_points <= 0:
            break

    # After combat ends
    if hero.health_points > 0:
        print(f"All enemies defeated! Hero {hero.name} survives with {hero.health_points} HP.")

    save_game(hero)


# Run the game
if __name__ == "__main__":
    main()
