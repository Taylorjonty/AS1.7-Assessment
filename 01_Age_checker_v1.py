# This component will be at the very start of the game. it will also check if the player is in primary school

user_name = ""
user_age = 0
while user_age != 1000:
    user_age = int(input("please enter your age: "))
    if user_age < 5 or user_age > 12:
        print("you can't play the game, you are not in primary school")
        print("STOP THE GAME")
        print()
    else:
        print("Rest of the game will go here")
        print()



