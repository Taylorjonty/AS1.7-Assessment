def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        # If the answer is yes, continue
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        # If the answer is no, show the instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            print("*** instructions ***")
            print()
            print("### How to play ###")
            return answer
        # Tell player to answer yes or no
        else:
            print("Please answer 'yes' or 'no'")
            print()


def ask_level():
    l_choice_local = input("What difficulty level would you like.\n""\nPress E for easy or H for hard: ").lower()
    if l_choice_local == "e":
        l_choice_local = "easy"
    else:
        l_choice_local = "hard"

    return l_choice_local


def levels():
        if l_choice_local == "easy":
            rounds = 10
            print(f"You have {rounds} rounds")
        else:
            rounds = 20
            print(f"You have {rounds} rounds")


def age_checker(question_text):
    while True:

        age = int(input(question_text))

        if age >= 12 or age <= 5:
            print("You are not on primary school so you can't play")
            exit()

        else:
            playability = "Can"
            return playability


# Ask if the person has played before
# Welcome the player to the game
print("Welcome to the maori language quiz!")
print()
# Ask what the players name is
user_name = input("What is your name: ")
# Say hello to the player
print(f"Hello {user_name}")
# Asks and checks that the player is in primary school
playability_ = age_checker("How old are you: ")
print(f"you {playability_} play this game.")
# Asks if the player has played before and will need instructions
show_instruction = yes_no("Have you played this game before: ")
print()
l_choice_local = ask_level()
print(f"{l_choice_local}")
levels()
print("Lets Go!")



