# this component finds out if the player wants to play easy mode or hard mode. it has been turned into a function
# based on 03_level_choice_v1
def ask_level():
    l_choice_local = input("What difficulty level would you like.\n""\nPress E for easy or H for hard: ").lower()
    if l_choice_local == "e":
        l_choice_local = "easy"
    else:
        l_choice_local = "hard"

    return l_choice_local


# main routine
l_choice_local = ask_level()
print(f"{l_choice_local} mode selected")

