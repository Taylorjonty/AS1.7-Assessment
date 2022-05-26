# Component is an improvement of 05_question_generator_v2
# This time it is turned into to functions

import random


def generate_question_easy():
    rounds = 1
    easy_question = ["tahi", "Rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    # Answers
    e_answer = ""
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

    print(f"You got {points} out of 10")


def generate_question_hard():
    rounds = 1
    hard_question = ["tahi", "Rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau", "tekau ma tahi",
                     "tekau ma rua", "tekau ma toru", "tekau ma wha", "tekau ma rima", "tekau ma ono", "tekau ma whitu",
                     "tekau ma waru", "tekau ma iwa", "rua tekau"]
    h_question = 0
    h_answer = ""
    points = 0
    while rounds <= 20:
        h_question = random.randint(1, 20)
        h_result = (hard_question[h_question - 1])
        h_answer = int(input(f"What does {h_result} mean: "))
        if h_answer == h_question:
            print("Correct")
            points += 1
            rounds += 1
        else:
            print("incorrect")
            rounds += 1

    print(f"You got {points} out of 20")


# main routine

# Enter the level
mode = input("Enter Mode: ").lower()
print()
# If it's easy, play this code
if mode == "easy":
    generate_question_easy()
else:
    generate_question_hard()


