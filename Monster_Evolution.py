# Monster_Evolution.py

def evolve_monster(monster, consecutive_wins):
    """
    Increase monster stats if the hero has 3 or more consecutive wins.
    +2 combat_strength and +5 health_points if condition is met.
    """
    if consecutive_wins >= 3:
        print("🔥 Monster is evolving due to Hero's win streak!")
        monster.combat_strength += 2
        monster.health_points += 5
