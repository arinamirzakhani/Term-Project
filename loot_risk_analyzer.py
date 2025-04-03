from hero import Hero

def loot_risk_analyzer(belt: list, hero: Hero, monster_power: str) -> list:
    print("\n--- Loot Risk Analysis ---")

    analyzable_item_types = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]

    items_to_analyze = [item for item in belt if item in analyzable_item_types]

    if not items_to_analyze:
        print(" No relevant items found in belt for analysis.")
        return items_to_analyze

    print(" Analyzing items in your belt:")
    for item in items_to_analyze:
        if item == "Health Potion":
            # Nested condition based on hero's health
            if hero.health_points < 50:
                print(f"  ✅ Health Potion: Your HP is low ({hero.health_points}). Consider using now!")
            elif hero.health_points == 100:
                print(f"  🧪 Health Potion: Your HP is full. Save for later.")
            else:
                print(f"  🧪 Health Potion: Your HP is {hero.health_points}. Save for later.")

        elif item == "Leather Boots":
            # Nested condition based on monster's power
            if monster_power == "Freeze Time":
                print(f"  👢 Leather Boots: Monster uses Freeze Time. Equip now for better mobility!")
            else:
                # Could add more conditions, e.g., if monster uses 'Acid Spit', maybe boots help?
                print(f"  👢 Leather Boots: Monster power is '{monster_power}'. Keep equipped or in inventory.")

        elif item == "Poison Potion":
            # This item is generally bad, advice is constant
            print(f"  ☠️ Poison Potion: Dangerous! Avoid using. Consider discarding.")

        elif item == "Secret Note":
            # Advice might depend on game context, keeping it simple
            print(f"  📜 Secret Note: Content unknown. Keep safe, examine when not in immediate danger.")

        elif item == "Flimsy Gloves":
            # Minor item, could add conditions if it counters a specific power later
            print(f"  🧤 Flimsy Gloves: Offers minimal protection. Keep in inventory for now.")

        # Add more elif blocks here if other analyzable_item_types are added later

    print("--- End Analysis ---")
    return items_to_analyze  # Return the list of items that were analyzed
