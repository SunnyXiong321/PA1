import time

#Full Year Schedule
year_schedule = {
    "Mod 1": {"A Block": "Global", "B Block": "Free Block", "C Block": "Chemistry"},
    "Mod 2": {"A Block": "Computer Science II", "B Block": "English", "C Block": "ISE"},
    "Mod 3": {"A Block": "Chemistry", "B Block": "English", "C Block": "Math"},
    "Mod 4": {"A Block": "Global", "B Block": "Math", "C Block": "ISE"},
    "Mod 5": {"A Block": "Co-curric", "B Block": "Co-curric", "C Block": "Co-curric"},  # Locked
    "Mod 6": {"A Block": "Global", "B Block": "Chemistry", "C Block": "ISE"},
    "Mod 7": {"A Block": "Math", "B Block": "English", "C Block": "Forensic Science"}
}

# Display full schedule
def show_schedule():
    print("\n📚 FULL Year Schedule:")
    for mod, blocks in year_schedule.items():
        print(f"\n🗂️ {mod}:")
        for block, course in blocks.items():
            print(f"  {block}: {course}")
    print()

# Display one mod only
def show_one_mod(mod_name):
    print(f"\n🔍 Updated Schedule for {mod_name}:")
    for block, course in year_schedule[mod_name].items():
        print(f"  {block}: {course}")
    print()

# Main Program
def main():
    print("🎉 Welcome to Sunny's Sophomore Year Schedule Manager!")
    time.sleep(0.5)
    show_schedule()

    has_edited = False

    while True:
        # Menu options depending on whether edits were made
        if has_edited:
            print("\n📌 Options: view, add, drop, change, or finish.")
        else:
            print("\n📌 Options: add, drop, change, or finish.")

        action = input("What would you like to do? ").strip().lower()

        # FINISH
        if action == "finish":
            print("🛑 Finishing up and locking your schedule...")
            time.sleep(0.5)
            show_schedule()
            print("✅ Final schedule locked in. You’re all set for the year, Sunny! 🌟")
            break

        valid_actions = {"add", "drop", "change", "view"}
        if action not in valid_actions or (not has_edited and action == "view"):
            print("❌ Invalid input. Try again.")
            continue

        mod_choice = input("Which Mod do you want to modify? (e.g., Mod 3): ").strip().title()
        block_choice = input("Which Block in that Mod? (A Block, B Block, or C Block): ").strip().title()

        valid_blocks = {"A Block", "B Block", "C Block"}
        if mod_choice not in year_schedule or block_choice not in valid_blocks:
            print("⚠️ Invalid Mod or Block name.")
            continue

        current_class = year_schedule[mod_choice][block_choice]

        #MOD 5 cocurric
        if mod_choice == "Mod 5":
            print("🚫 Mod 5 is reserved for Co-curric. Cannot be modified.")
            continue

        #DROP
        if action == "drop":
            if current_class == "—":
                print("⚠️ That block is already empty.")
            elif current_class.lower() == "co-curric":
                print("🔒 Co-curric blocks are locked.")
            else:
                confirm = input(f"Are you sure you want to drop '{current_class}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    year_schedule[mod_choice][block_choice] = "—"
                    print(f"✅ Dropped '{current_class}' from {mod_choice} {block_choice}.")
                    has_edited = True
                    show_one_mod(mod_choice)
                    time.sleep(0.3)
                    show_schedule()
                else:
                    print("❎ Drop canceled.")

        #ADD
        elif action == "add":
            if current_class != "—" and current_class.lower() != "free block":
                print(f"🛑 That block already has '{current_class}'. Drop it first.")
            else:
                new_class = input("What class do you want to add? ").strip()
                if not new_class:
                    print("❌ Cannot add an empty class.")
                else:
                    year_schedule[mod_choice][block_choice] = new_class
                    print(f"✅ Added '{new_class}' to {mod_choice} {block_choice}.")
                    has_edited = True
                    show_one_mod(mod_choice)
                    time.sleep(0.3)
                    show_schedule()

        #CHANGE
        elif action == "change":
            if current_class.lower() == "co-curric":
                print("🔒 Cannot change Co-curric blocks.")
            else:
                new_class = input(f"What class do you want instead of '{current_class}'? ").strip()
                if not new_class:
                    print("❌ Cannot enter an empty class name.")
                else:
                    year_schedule[mod_choice][block_choice] = new_class
                    print(f"✅ Changed {mod_choice} {block_choice} from '{current_class}' to '{new_class}'.")
                    has_edited = True
                    show_one_mod(mod_choice)
                    time.sleep(0.3)
                    show_schedule()

#Run Program
if __name__ == "__main__":
    main()