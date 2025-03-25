import random
import pickle
import os
import platform


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
        self._health_points = max(0, value)

    def __del__(self):
        print(f"A {self.__class__.__name__} object is being destroyed by the garbage collector.")


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
        super().__del__()  # Explicitly call parent destructor


class Monster(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"A wild Monster {self.name} appears!")

    def monster_attacks(self, hero):
        try:
            if not isinstance(hero, Hero):
                raise TypeError("The target must be a Hero instance.")
            if not isinstance(hero.health_points, int):
                raise ValueError("Hero's health points must be an integer.")

            if hero.health_points > 0:
                damage = random.randint(1, 10)
                print(f"Monster {self.name} attacks and deals {damage} damage!")
                hero.health_points = max(0, hero.health_points - damage)
        except Exception as e:
            print(f"Error in monster_attacks: {e}")

    def __del__(self):
        print(f"The Monster {self.name} object is being destroyed by the garbage collector.")
        super().__del__()


def save_game(hero, monsters_killed):
    with open('hero_save.pkl', 'wb') as file:
        pickle.dump(hero, file)
    with open('save.txt', 'w') as file:
        file.write(f"Monsters Killed: {monsters_killed}\n")
    print("Game saved successfully!")


def load_game():
    try:
        with open('hero_save.pkl', 'rb') as file:
            hero = pickle.load(file)
        print(f"Game loaded. Welcome back, Hero {hero.name}!")
        return hero
    except FileNotFoundError:
        print("No saved game found.")
        return None


def get_monsters_killed():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Monsters Killed" in line:
                    return int(line.split(":")[1].strip())
    except FileNotFoundError:
        return 0


def main():

    hero = load_game()
    if hero is None:
        hero_name = input("Enter your Hero's name: ")
        hero = Hero(hero_name)


    monster_name = "Goblin"
    monster = Monster(monster_name)


    monsters_killed = get_monsters_killed()

    while hero.health_points > 0 and monster.health_points > 0:
        print("\n--- Combat Begins ---")
        hero.hero_attacks(monster)
        if monster.health_points <= 0:
            print(f"{monster.name} is dead!")
            monsters_killed += 1
            break

        monster.monster_attacks(hero)
        if hero.health_points <= 0:
            print(f"{hero.name} is dead!")
            break


    save_game(hero, monsters_killed)


if __name__ == "__main__":
    main()
