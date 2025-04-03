import random
import pickle
from hero import Hero


def save_game(winner, hero, num_stars, monsters_killed):
    with open("save.txt", "w") as file:
        file.write(f"Winner: {winner}\n")
        file.write(f"Hero: {hero.name}\n")
        file.write(f"Stars: {num_stars}\n")
        file.write(f"Monsters Killed: {monsters_killed}\n")
        file.write(f"Gold: {hero.gold}\n")

    with open("hero_save.pkl", "wb") as file:
        pickle.dump(hero, file)

    print("Game saved successfully!")


def load_game():
    try:
        with open("hero_save.pkl", "rb") as file:
            hero = pickle.load(file)
            if isinstance(hero, Hero):
                print("    |    Loading from saved file ...")
                print(f"🪙 Gold: {hero.gold}")
                return hero
            else:
                print(" Warning: Loaded object is not a Hero!")
                return None
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


def adjust_combat_strength(hero_combat_strength, monster_combat_strength):
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            for line in lines:
                if "Stars" in line:
                    num_stars = int(line.split(":")[1].strip())
                    if num_stars > 3:
                        print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                        monster_combat_strength += 1
                elif "Winner" in line and "Monster" in line:
                    print("    |    ... Increasing the hero's combat strength since you lost last time")
                    hero_combat_strength += 1
    except FileNotFoundError:
        print("No previous game found. Combat strength remains unchanged.")


def use_loot(belt, health_points, max_potions=5):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        if belt.count("Health Potion") < max_potions:
            health_points = min(20, (health_points + 2))
            print(f"    |    You used {first_item} to up your health to {health_points}")
        else:
            print("    |    You cannot carry more health potions.")
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print(f"    |    You used {first_item} to hurt your health to {health_points}")
    else:
        print(f"    |    You used {first_item} but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt, max_potions=5):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @               
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)

    if loot == "Health Potion" and belt.count("Health Potion") < max_potions:
        belt.append(loot)
        print(f"    |    You added a Health Potion to your belt.")
    elif loot == "Health Potion":
        print(f"    |    You cannot carry more Health Potions!")
    else:
        belt.append(loot)
        print(f"    |    You added {loot} to your belt.")

    print("    |    Your belt: ", belt)
    return loot_options, belt


def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                  @@   @@ 
                                  @    @  
                                  @   @   
                 @@@@@@          @@  @    
              @@       @@        @ @@     
             @%         @     @@@ @       
              @        @@     @@@@@     
                 @@@@@        @@       
                 @    @@@@                
            @@@ @@                        
         @@     @                         
     @@*       @                          
     @        @@                          
             @@                                                     
           @   @@@@@@@                    
          @            @                  
        @              @                 
    """
    print(ascii_image)
    print(f"    |    Player's weapon ({combat_strength}) ---> Monster ({m_health_points})")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength
        print(f"    |    You have reduced the monster's health to: {m_health_points}")
    return m_health_points


def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
              @@@@ @                           
         (     @*&@  ,                          
       @               %                       
        &#(@(@%@@@@@*   /                      
         @@@@@.                                
                  @       /                   
                   %         @                 
               ,(@(*/           %              
                  @ (  .@#                 @   
                             @           .@@. @
                      @         ,              
                         @       @ .@          
                                @              
                             *(*  *      
                """
    print(ascii_image2)
    print(f"    |    Monster's Claw ({m_combat_strength}) ---> Player ({health_points})")
    if m_combat_strength >= health_points:
        health_points = 0
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength
        print(f"    |    The monster has reduced Player's health to: {health_points}")
    return health_points


def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + inception_dream(num_dream_lvls - 1)