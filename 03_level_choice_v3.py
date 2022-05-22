# this component finds out if the player wants to play easy mode or hard mode. it has been turned into a function
# based on 03_level_choice_v1
def ask_level():
    l_choice_local = ""
    l_choice_local = input("What difficulty level would you like.\n""\nPress E for easy or H for hard: ").lower()
    while l_choice_local != "easy" or l_choice_local != "hard":
        if l_choice_local == "e":
            l_choice_local = "easy"
            break
        elif l_choice_local == "h":
            l_choice_local = "hard"
            break
        else:
            print("Enter E or H ")
            break

    return l_choice_local


# main routine
l_choice_local = ask_level()
print(f"{l_choice_local} mode selected")

