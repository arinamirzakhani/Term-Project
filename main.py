import os
import platform
import random
import functions  # Your helper functions file
from hero import Hero
from monster import Monster
from merchant import Merchant
from loot_risk_analyzer import loot_risk_analyzer

# Helper function to check health and offer potion
def check_and_offer_potion(hero):
    if hero.health_points == 0:
        print("💀 Hero is dead.")
    elif hero.health_points < 50 and (hero.potions > 0 or "Health Potion" in hero.belt):
        print(f"⚠️ Hero's health is low! (HP: {hero.health_points})")
        use_potion = input("Do you want to use a health potion? (y/n): ").strip().lower()
        if use_potion == "y":
            hero.use_health_potion()
        else:
            print("⚠️ No potion used.")
    else:
        print("Hero is in good shape.")

# System info
print(f"🖥️ Operating System: {os.name}")
print(f"🐍 Python Version: {platform.python_version()}")

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

num_stars = 0
monsters_killed = functions.get_monsters_killed()

hero = functions.load_game()
if not isinstance(hero, Hero):
    print("There is no hero added yet!")
    hero = Hero("Unnamed Hero")

# Get combat strengths
for i in range(5):
    print("\n⚔️ Enter your combat strength (1-6): ", end="")
    combat_strength = input()
    print("👹 Enter the monster's combat strength (1-6): ", end="")
    m_combat_strength = input()

    if combat_strength.isnumeric() and m_combat_strength.isnumeric():
        combat_strength = int(combat_strength)
        m_combat_strength = int(m_combat_strength)
        if 1 <= combat_strength <= 6 and 1 <= m_combat_strength <= 6:
            break
    print("❌ Invalid input! Enter numbers between 1 and 6.")

# Weapon assignment
print("\n🎲 Rolling for weapon... (Press Enter)")
input()

ascii_weapon = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
"""
print(ascii_weapon)

weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, combat_strength + weapon_roll)
print(f"🔫 Hero's weapon: {weapons[weapon_roll - 1]}")
functions.adjust_combat_strength(combat_strength, m_combat_strength)

# Assign health
print("\n🎲 Rolling for health points... (Press Enter)")
input()
hero.health_points = random.choice(big_dice_options)
print(f"❤️ Hero's HP: {hero.health_points}")

print("\n🎲 Rolling for monster health points... (Press Enter)")
input()
m_health_points = random.choice(big_dice_options)
print(f"👹 Monster's HP: {m_health_points}")

# Dream levels
while True:
    try:
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
        num_dream_lvls = int(num_dream_lvls)
        if 0 <= num_dream_lvls <= 3:
            break
        else:
            print("⚠️ Number entered must be between 0 and 3.")
    except ValueError:
        print("⚠️ Invalid input! Please enter a whole number between 0 and 3.")

dream_result = functions.inception_dream(num_dream_lvls)
print(f"🌀 You returned from the dream with result: {dream_result}")

# Merchant and loot
merchant = Merchant("Old Merchant")
merchant.sell_health_potion(hero)

print("\n🎒 You find a loot bag! Collecting items...")
loot_options, belt = functions.collect_loot(loot_options, belt)
loot_options, belt = functions.collect_loot(loot_options, belt)
belt.sort()
print(f"🎒 Your organized belt: {belt}")

belt, hero.health_points = functions.use_loot(belt, hero.health_points)

# Monster magic
print("🎲 Rolling for Monster's Magic Power... (Press Enter)")
input()

ascii_magic = """
                @%   @                      
         @     @                         
             &                           
      @      .                            
     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                 
"""
print(ascii_magic)

power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
print(f"🔥 The monster's combat strength is now {m_combat_strength} using {power_roll} magic power!")

# --- Analyse Loot ---
loot_risk_analyzer(hero.belt, hero, power_roll)

# Battle begins
monster = Monster("Goblin")
print("\n⚔️ Battle begins!")

while hero.health_points > 0:
    print("\n🎲 Rolling for first strike... (Press Enter)")
    input()
    attack_roll = random.choice(small_dice_options)

    if attack_roll % 2 != 0:
        print("🗡️ Hero strikes!")
        m_health_points = functions.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            monsters_killed += 1
            monster.drop_loot(hero)
            break

        check_and_offer_potion(hero)
        print("\n🔥 Monster strikes back!")
        hero.health_points = functions.monster_attacks(m_combat_strength, hero.health_points)

    else:
        print("🔥 Monster strikes!")
        hero.health_points = functions.monster_attacks(m_combat_strength, hero.health_points)

        if hero.health_points == 0:
            num_stars = 1
            break

        check_and_offer_potion(hero)
        print("\n🗡️ Hero strikes back!")
        m_health_points = functions.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            monsters_killed += 1
            monster.drop_loot(hero)
            break

if hero.health_points == 0:
    print("💀 Hero has fallen... Game Over!")

winner = "Hero" if m_health_points <= 0 else "Monster"
print(f"\n🏆 {winner} wins the battle!")

# Hero name input
tries = 0
while True:
    hero_name = input("Enter your Hero's name (in two words): ").strip()
    name_parts = hero_name.split()
    if len(name_parts) != 2:
        print("⚠️ Please enter a name with two words.")
        tries += 1
    elif not name_parts[0].isalpha() or not name_parts[1].isalpha():
        print("⚠️ Only letters are allowed.")
        tries += 1
    else:
        short_name = name_parts[0][:2] + name_parts[1][0]
        print(f"👑 I'll call you {short_name} for short.")
        hero.name = short_name
        break

# Save game
stars_display = "*" * num_stars
print(f"⭐ Hero {short_name} earns {stars_display} stars!")
functions.save_game(winner, hero, num_stars, monsters_killed)