place = input("Choose a place: forest or cave? ")

# Consistent indentation and input validation
if place.lower() == "forest":
    action = input("Climb a tree or cross a river? ")

    if action.lower() == "climb a tree":
        print("You found a bird's nest!")
    elif action.lower() == "cross a river":
        danger_check = input("Do you see any danger in the river (yes/no)? ").lower()
        if "danger" in danger_check:
            print("Oh no! You encounter a crocodile while crossing and barely escape!")
        else:
            print("You found a sturdy boat and safely crossed the river!")

elif place.lower() == "cave":
    explore_choice = input("Do you want to explore deeper (yes/no)? ").lower()
    if "explore" in explore_choice:
        print("You ventured deeper and discovered a hidden chamber filled with gold!")
    else:
        print("You find a small treasure chest near the entrance.")

else:
    print("Invalid choice. Please choose 'forest' or 'cave'.")