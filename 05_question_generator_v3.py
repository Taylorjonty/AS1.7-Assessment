# Component is an improvement of 05_question_generator_v1
# This one uses lists instead of individual if statements

import random
# Questions
easy_question = ["tahi", "Rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
# Answers
easy_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e_answer = ""
e_question = 0
hard_question = ["tahi", "Rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau", "tekau ma tahi",
                 "tekau ma rua", "tekau ma toru", "tekau ma wha", "tekau ma rima", "tekau ma ono", "tekau ma whitu",
                 "tekau ma waru", "tekau ma iwa", "rua tekau"]
hard_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
h_question = 0
h_answer = ""
top_number = 10
round_ = 1

# Enter the level
mode = input("Enter Mode: ").lower()
print()
# If it's easy, play this code
if mode == "easy":
    while round_ <= 10:
        e_question = random.randint(1, 10)
        print(easy_question[e_question - 1])
        round_ += 1
# if it's hard, play this code
elif mode == "hard":
    while round_ <= 20:
        h_question = random.randint(1, 20)
        print(hard_question[h_question - 1])
        round_ += 1

else:
    print("?")
