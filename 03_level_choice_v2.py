# this component finds out if the player wants to play easy mode or hard mode
# based on 03_level_choice_v1 but this time

choice = ""
l_choice = ""

# Asks whether the player wants to play easy or hard mode (part 1)
print("Would you like easy or hard mode?")
# While there is no answer entered repeat the loop
while l_choice != "e" or l_choice != "h":
    # Asks whether the player wants to play easy or hard mode (part 2)
    l_choice = input("Press E for easy mode. Press H for hard mode: ").lower()
    # if the player answer is easy play this part
    if l_choice == "e" or l_choice == "easy":
        choice = "Easy"
        break
    # if the player answer is hard play this part
    elif l_choice == "h" or l_choice == "hard":
        choice = "Hard"
        break
    # if the player answer is not either, redo loop
    else:
        print("please choose easy or hard by pressing E or H")


print(f"You chose {choice} mode")
