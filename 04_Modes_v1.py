# This component starts after the player selects Easy mode or hard mode from the function in 03_level_choice_3
l_choice = ""

# While the player hasn't entered e or h
while l_choice != "e" or l_choice != "h":

    l_choice = input("E for easy mode, H for hard mode ").lower()
    # if the player chose easy mode. They have 10 rounds
    if l_choice == "e":
        rounds = 10
        print(f"You have {rounds} rounds")
        # if the player chose hard mode. They have 20 rounds
    else:
        rounds = 20
        print(f"You have {rounds} rounds")


