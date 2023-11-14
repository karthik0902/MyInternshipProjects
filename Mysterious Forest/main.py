import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    time.sleep(1)
    print("You find yourself at the edge of a mysterious forest.")
    time.sleep(1)
    print("Your objective is to navigate through the forest and reach the other side.")
    time.sleep(1)

def make_choice(options):
    while True:
        print("Choose your path:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You enter the forest and come across a fork in the path.")
    time.sleep(1)
    options = ["Take the left path", "Take the right path"]
    choice = make_choice(options)

    if choice == 1:
        print("You chose the left path. It leads you to a clearing.")
        time.sleep(1)
        return "clearing"
    elif choice == 2:
        print("You chose the right path. It leads you deeper into the forest.")
        time.sleep(1)
        return "deep_forest"

def clearing():
    print("In the clearing, you see a magical fountain.")
    time.sleep(1)
    options = ["Drink from the fountain", "Continue on the path"]
    choice = make_choice(options)

    if choice == 1:
        print("You drink from the fountain and feel revitalized.")
        time.sleep(1)
        return "win"
    elif choice == 2:
        print("You decide to continue on the path.")
        time.sleep(1)
        return "continue"

def deep_forest():
    print("As you venture deeper into the forest, you encounter a mysterious creature.")
    time.sleep(1)
    options = ["Try to communicate with the creature", "Run away"]
    choice = make_choice(options)

    if choice == 1:
        print("You attempt to communicate with the creature, and it leads you to a hidden passage.")
        time.sleep(1)
        return "hidden_passage"
    elif choice == 2:
        print("You run away from the creature, but you get lost in the forest.")
        time.sleep(1)
        return "lost"

def hidden_passage():
    print("The hidden passage takes you to a shortcut.")
    time.sleep(1)
    print("You reach the other side of the forest successfully.")
    time.sleep(1)
    return "win"

def lost():
    print("You are lost in the forest and unable to find your way out.")
    time.sleep(1)
    print("Unfortunately, you did not make it to the other side.")
    time.sleep(1)
    return "lose"

def main():
    introduction()

    current_location = "forest_path"
    while True:
        if current_location == "forest_path":
            current_location = forest_path()
        elif current_location == "clearing":
            current_location = clearing()
        elif current_location == "deep_forest":
            current_location = deep_forest()
        elif current_location == "hidden_passage":
            current_location = hidden_passage()
        elif current_location == "lost":
            current_location = lost()
        elif current_location == "win":
            print("Congratulations! You successfully navigated through the mysterious forest.")
            break

if __name__ == "__main__":
    main()
