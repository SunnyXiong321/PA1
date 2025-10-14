# Write a small program that allows people to add, drop, and change their mod2 schedule
import time

mod2 = {
    "A Block": "CS2",
    "B Block": "English",
    "C Block": "ISE"
}

def show_schedule():
    print("\n📚 This is your Mod 2 schedule:")
    for block, course in mod2.items():
        print(f"  {block}: {course}")
    print()  # blank line for readability


def main():
    show_schedule()
    time.sleep(1)

    while True:  # <--- keeps the program running until user chooses to quit
        change = input("Do you want to change anything? You can add, drop, or change any classes! (y/n)\nYour choice: ").strip().lower()

        if change == "y":
            adc = input("Do you want to add, drop, or change?\nYour choice: ").strip().lower()
            valid_actions = {"add", "drop", "change"}

            if adc not in valid_actions:
                print("❌ That's not a valid choice, please try again.")
                continue  # go back to the top of the while loop

            if adc == "add":
                print("Um, you don't have a free block, so no adding for now.")

            elif adc == "drop":
                dropping = input("What block do you wanna drop? (e.g., A Block) ").strip().title()
                if dropping in mod2:
                    removed = mod2.pop(dropping)
                    print(f"✅ Dropped {removed} from {dropping}.")
                else:
                    print("That block doesn't exist.")

            elif adc == "change":
                changing = input("What block do you wanna change? (e.g., B Block) ").strip().title()
                if changing in mod2:
                    new_class = input(f"What class do you want instead of {mod2[changing]}? ").strip()
                    mod2[changing] = new_class
                    print(f"✅ Changed {changing} to {new_class}.")
                else:
                    print("That block doesn't exist.")

            # Show updated schedule every time
            show_schedule()

        elif change == "n":
            print("Okay bye 👋")
            break  # exit the while loop cleanly

        else:
            print("❌ Please only type 'Y' or 'N'.")

if __name__ == "__main__":
    main()