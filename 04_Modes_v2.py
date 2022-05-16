# This component starts after the player selects Easy mode or hard mode from the function in 03_level_choice_3
# it is based off 04_Modes_v2


def levels():
    l_choice = ""
    while l_choice != "e" or l_choice != "h":
        l_choice = input("E for easy mode, H for hard mode ").lower()
        if l_choice == "e":
            rounds = 10
            print(f"You have {rounds} rounds")
        else:
            rounds = 20
            print(f"You have {rounds} rounds")

# main routine
levels()
