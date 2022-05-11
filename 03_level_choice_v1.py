# This component finds out if the player wants to play easy mode or hard mode

choice = ""
l_choice = ""

# Asks whether the player wants to play easy or hard mode (part 1)
print("Would you like easy or hard mode?")
# While there is no answer entered repeat the loop
while l_choice != "easy" or l_choice != "hard":
    # Asks whether the player wants to play easy or hard mode (part 2)
    l_choice = input("Type Easy for easy mode. Type Hard for hard mode: ").lower()
    # if the player answer is easy play this part
    if l_choice == "easy":
        choice = "Easy"
        break
    # if the player answer is hard play this part
    elif l_choice == "hard":
        choice = "Hard"
        break
    # if the player answer is not either, redo loop
    else:
        print("please choose easy or hard")


print(f"You chose {choice} mode")
