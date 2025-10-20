'''
setting up a version of PA1 that uses file instead of dictionaries
'''

# Sophomore Schedule Manager
import time

# Define your full year schedule
schedule = {
   }

seasons = {
    "Fall": ["Mod 1", "Mod 2", "Mod 3"],
    "Winter": ["Mod 4", "Mod 5"],
    "Spring": ["Mod 6", "Mod 7"]
}

#define some mod names so the user have the freedom to type whatever they want
mod_names = {
    "1": "Mod 1", "mod1": "Mod 1", "mod 1": "Mod 1",
    "2": "Mod 2", "mod2": "Mod 2", "mod 2": "Mod 2",
    "3": "Mod 3", "mod3": "Mod 3", "mod 3": "Mod 3",
    "4": "Mod 4", "mod4": "Mod 4", "mod 4": "Mod 4",
    "5": "Mod 5", "mod5": "Mod 5", "mod 5": "Mod 5",
    "6": "Mod 6", "mod6": "Mod 6", "mod 6": "Mod 6",
    "7": "Mod 7", "mod7": "Mod 7", "mod 7": "Mod 7"
}

block_names = {
    "a": "A Block", "a block": "A Block",
    "b": "B Block", "b block": "B Block",
    "c": "C Block", "c block": "C Block",
    "d": "D Block", "d block": "D Block"
}

def show_schedule():
    print("\n📚 Here is your 2025-2026 school year schedule:")
    for mod, blocks in schedule.items():
        print(f"\n😺 {mod}:")
        for block, course in blocks.items():
            print(f"  {block}: {course}")
    print()

#show schedule of that one mod after a change
def show_mod_schedule(mod):
    print(f"\n📅 {mod} Schedule:")
    for block, course in schedule[mod].items():
        print(f"  {block}: {course}")

def get_season_by_mod(mod):
    for season, mods in seasons.items():
        if mod in mods:
            return season
    return None

#show schedule of the season after a change
def show_dblock_season(season):
    print(f"\n📆 D Block Schedule for {season} season:")
    for mod in seasons[season]:
        print(f"  {mod} D Block: {schedule[mod]['D Block']}")

def main():
    print("🎉 Welcome to Sunny's Sophomore Year Schedule Manager!")
    time.sleep(1)
    show_schedule()
    time.sleep(2)

    while True:
        print("\n Options ~ you can: add, drop, change, or finish (end and display final schedule).")
        action = input("What would you like to do? ").strip().lower()

        if action == "finish":
            print("\n✅ Final Schedule:")
            show_schedule()
            break

        if action not in ["add", "drop", "change"]:
            print("❌ Invalid action. Please choose from add, drop, change, or finish.")
            continue

        # loop until valid mod
        while True:
            mod_input = input("Which Mod do you want to modify? (e.g., Mod 3 or just 3): ").strip().lower().replace(" ", "")
            if mod_input in mod_names:
                mod = mod_names[mod_input]
                break
            else:
                print("⚠️ Invalid Mod. Try again.")

        # loop until valid block
        while True:
            block_input = input("Which Block in that Mod? (A, B, C, or D): ").strip().lower()
            if block_input in block_names:
                block = block_names[block_input]
                break
            else:
                print("⚠️ Invalid Block. Try again.")

        current = schedule[mod][block]

        if block == "D Block" and action != "change":
            print("❌ You cannot add or drop D Block. You may only change it.")
            continue

        if block == "D Block" and action == "change":
            print("⚠️ Remember that D Blocks are seasonal. Changing it this mod will update the whole season!")
            new_class = input(f"What D Block activity do you want instead of '{current}'? ").strip()
            season = get_season_by_mod(mod)
            for m in seasons[season]:
                schedule[m]["D Block"] = new_class
            show_dblock_season(season)
            continue

        if mod == "Mod 5" and block in ["A Block", "B Block", "C Block"]:
            print("🚫 You cannot modify Co-curric blocks in Mod 5.")
            continue

        if action == "drop":
            schedule[mod][block] = "Free Block"
            print(f"✅ Dropped '{current}' from {mod} {block}.")

        elif action == "add":
            if current != "Free Block":
                print("🛑 That block already has a class. Drop it first to add a new one.")
                continue
            new_class = input("What class do you want to add? ").strip()
            schedule[mod][block] = new_class
            print(f"✅ Added '{new_class}' to {mod} {block}.")

        elif action == "change":
            new_class = input(f"What class do you want instead of '{current}'? ").strip()
            schedule[mod][block] = new_class
            print(f"✅ Changed {mod} {block} from '{current}' to '{new_class}'.")

        show_mod_schedule(mod)

if __name__ == "__main__":
    main()