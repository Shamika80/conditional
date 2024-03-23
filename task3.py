place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
    action = input("Climb a tree or cross a river? ").lower()

    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        danger_check = input("Do you see any danger in the river (yes/no)? ").lower()
        if "danger" in danger_check:
            print("Oh no! You encounter a crocodile while crossing and barely escape!")
        else:
            print("You found a sturdy boat and safely crossed the river!")
    else:
        pass  

elif place == "cave":
    
    cave_action = input("Do you want to light a torch or proceed in the dark (torch/dark)? ").lower()

    if cave_action == "torch":
        print("You light your torch and cautiously venture deeper.")
        explore_choice = input("Do you want to explore deeper (yes/no)? ").lower()
        if "explore" in explore_choice:
            print("You ventured deeper and discovered a hidden chamber filled with gold!")
        else:
            print("You find a small treasure chest near the entrance containing a mysterious scroll.")
    elif cave_action == "dark":
        print("You feel a cold wind as you enter the darkness. Visibility is limited.")
    
        if "danger" in input("You hear a strange noise! (yes/no)? ").lower():
            print("A creature lunges from the shadows! You barely escape with a scratch.")
        else:
            print("Despite the darkness, you manage to find a small treasure chest near the entrance.")
            # Reduced reward for not using a torch (replace placeholder)
            print("However, the darkness seems to have dimmed the treasure's glow.")
    else:
        pass  # Invalid action at the cave entrance

else:
    print("Invalid choice. Please choose 'forest' or 'cave'.")