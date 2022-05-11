# this component finds out if the player wants to play easy mode or hard mode
# based on 03_level_choice_v1 but this time

choice = ""
l_choice = ""

print("Would you like easy or hard mode?")
while l_choice != "e" or l_choice != "h":
    l_choice = input("Press E for easy mode. Press H for hard mode: ").lower()
    if l_choice == "e":
        choice = "Easy"
        break
    elif l_choice == "h":
        choice = "Hard"
        break
    else:
        print("please choose easy or hard by pressing E or H")


print(f"You chose {choice} mode")
