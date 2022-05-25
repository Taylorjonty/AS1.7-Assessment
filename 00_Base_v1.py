import random


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
    l_choice_local = ""
    while l_choice_local != "easy" or l_choice_local != "hard":
        l_choice_local = input("What difficulty level would you like.\n""\nPress E for easy or H for hard: ").lower()
        if l_choice_local == "e":
            l_choice_local = "easy"
            break
        elif l_choice_local == "h":
            l_choice_local = "hard"
            break
        else:
            print("Enter E or H ")

    return l_choice_local


def levels():
    # If the level is easy, play ten rounds
    if l_choice_local == "easy":
        rounds = 10
        print(f"You have {rounds} rounds")
    # If the level is hard, play 20 rounds
    else:
        rounds = 20
        print(f"You have {rounds} rounds")


def generate_question_easy():
    rounds = 1
    easy_question = ["tahi", "Rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    # Answers
    e_answer = 0
    e_question = 0
    points = 0
    while rounds <= 10:
        e_question = random.randint(1, 10)
        e_result = (easy_question[e_question - 1])
        e_answer = int(input(f"What does {e_result} mean: "))
        if e_answer == e_question:
            print("Correct")
            points += 1
            rounds += 1
        else:
            print("incorrect")
            rounds += 1
    print(f"You got {points}/10")


def age_checker(question_text):
    while True:

        age = int(input(question_text))

        if age >= 13 or age <= 4:
            print("You are not on primary school so you can't play")
            exit()

        else:
            playability = "Can"
            return playability


def generate_question_hard():
    # Shows the first round
    rounds = 1
    # Here are the questions
    hard_question = ["tahi", "Rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau", "tekau ma tahi",
                     "tekau ma rua", "tekau ma toru", "tekau ma whā", "tekau ma rima", "tekau ma ono", "tekau ma whitu",
                     "tekau ma waru", "tekau ma iwa", "rua tekau"]
    h_question = 0
    h_answer = ""
    points = 0
    # While there is less than 20 rounds
    while rounds <= 20:
        h_question = random.randint(1, 10)
        h_result = (hard_question[h_question - 1])
        h_answer = int(input(f"What does {h_result} mean: "))
        if h_answer == h_question:
            print("Correct")
            points += 1
            rounds += 1
        else:
            print("incorrect")
            rounds += 1
    print(f"You got {points}/20")


# Main routine
print("Welcome to the maori language quiz!")
print()
# Ask what the players name is
user_name = input("What is your name: ")
# Say hello to the player
print(f"Hello {user_name}")
# Asks and checks that the player is in primary school
playability_ = age_checker("How old are you: ")
print(f"You {playability_} play this game.")
# Asks if the player has played before and will need instructions
show_instruction = yes_no("Have you played this game before: ")
print()
l_choice_local = ask_level()
print(f"{l_choice_local}")
levels()
print("Lets Go!")
# If it's easy, play this code
if l_choice_local == "easy":
    generate_question_easy()
else:
    generate_question_hard()
