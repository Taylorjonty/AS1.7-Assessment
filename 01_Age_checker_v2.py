# This component will be at the very start of the game. it will also check if the player is in primary school
# based off 01_age_checker_v1 but this time in a function

def age_checker(question_text):
    while True:

        age = int(input(question_text))

        if age >= 12 or age <= 5:
            print("You are not on primary school")
            exit()

        else:
            playability = "Yes"
            return playability


# main routine
playability_ = age_checker("How old are you: ")
print(f"you {playability_} play this game.")
