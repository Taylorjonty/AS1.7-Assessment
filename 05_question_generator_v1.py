import random

points = 0
rounds = 0

mode = input("What level do you want: ").lower()
if mode == "easy":
    print("Easy Mode")
    # When rounds gets to 10, then game will stop
    while rounds <= 9:
        number = random.randint(1, 10)
        # when the number is chosen, find the number and make that the question
        if number == 1:
            answer = 1
            player_answer = int(input("What does Tahi mean: "))
        elif number == 2:
            answer = 2
            player_answer = int(input("What does Rua mean: "))
        elif number == 3:
            answer = 3
            player_answer = int(input("What does Toru mean: "))
        elif number == 4:
            answer = 4
            player_answer = int(input("What does whā mean: "))
        elif number == 5:
            answer = 5
            player_answer = int(input("What does rima mean: "))
        elif number == 6:
            answer = 6
            player_answer = int(input("What does ono mean: "))
        elif number == 7:
            answer = 7
            player_answer = int(input("What does whitu mean: "))
        elif number == 8:
            answer = 8
            player_answer = int(input("What does waru mean: "))
        elif number == 9:
            answer = 9
            player_answer = int(input("What does iwa mean: "))
        else:
            answer = 10
            player_answer = int(input("What does tekau mean: "))
        # if the answer is correct, give them a point, and add a round
        if player_answer == answer:
            print("That's correct")
            points += 1
            print(f"you have {points} points")
            rounds += 1
            print()
        # if the answer is wrong, don't give them a point, then add a round
        else:
            print("that's wrong")
            rounds += 1
            print()
else:
    print("Hard Mode")
    while rounds <= 19:
        number = random.randint(1, 20)
        # when the number is chosen, find the number and make that the question
        if number == 1:
            answer = 1
            player_answer = int(input("What does Tahi mean: "))
        elif number == 2:
            answer = 2
            player_answer = int(input("What does Rua mean: "))
        elif number == 3:
            answer = 3
            player_answer = int(input("What does Toru mean: "))
        elif number == 4:
            answer = 4
            player_answer = int(input("What does whā mean: "))
        elif number == 5:
            answer = 5
            player_answer = int(input("What does rima mean: "))
        elif number == 6:
            answer = 6
            player_answer = int(input("What does ono mean: "))
        elif number == 7:
            answer = 7
            player_answer = int(input("What does whitu mean: "))
        elif number == 8:
            answer = 8
            player_answer = int(input("What does waru mean: "))
        elif number == 9:
            answer = 9
            player_answer = int(input("What does iwa mean: "))
        elif number == 10:
            answer = 10
            player_answer = int(input("What does tekau mean: "))
        elif number == 11:
            answer = 11
            player_answer = int(input("What does tekau ma tahi mean: "))
        elif number == 12:
            answer = 12
            player_answer = int(input("What does tekau ma rua mean: "))
        elif number == 13:
            answer = 13
            player_answer = int(input("What does tekau ma toru mean: "))
        elif number == 14:
            answer = 14
            player_answer = int(input("What does tekau ma whā mean: "))
        elif number == 15:
            answer = 15
            player_answer = int(input("What does tekau ma rima mean: "))
        elif number == 16:
            answer = 16
            player_answer = int(input("What does tekau ma ono mean: "))
        elif number == 17:
            answer = 17
            player_answer = int(input("What does tekau ma whitu mean: "))
        elif number == 18:
            answer = 18
            player_answer = int(input("What does tekau ma waru mean: "))
        elif number == 19:
            answer = 19
            player_answer = int(input("What does tekau ma iwa mean: "))
        else:
            answer = 20
            player_answer = int(input("What does rua tekau mean: "))
        # if the answer is correct, give them a point, and add a round
        if player_answer == answer:
            print("That's correct")
            points += 1
            print(f"you have {points} points")
            rounds += 1
            print()
        # if the answer is wrong, don't give them a point, then add a round
        else:
            print("that's wrong")
            rounds += 1
            print()

print(f"You got {points}/20")
