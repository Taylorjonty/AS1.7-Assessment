# this component finds out if the player wants to play easy mode or hard mode

choice = ""
l_choice = ""

print("Would you like easy or hard mode?")
while l_choice != "easy" or l_choice != "hard":
    l_choice = input("Type Easy for easy mode. Type Hard for hard mode: ").lower()
    if l_choice == "easy":
        choice = "Easy"
        break
    elif l_choice == "hard":
        choice = "Hard"
        break
    else:
        print("please choose easy or hard")


print(f"You chose {choice} mode")
