# This component will check if the player has played before
# It will also make sure that only yes or no in added

answer = ""

# Ask the player if they have played before
answer = (input("Have you played the game before: ")).lower()
# if the answer is yes, start the game.
if answer == "yes":
    print("program continues")
# if the answer is no, show the instructions
elif answer == "no":
    print("*** Instructions ***")
# Tells the player that they need to answer only yes or no
else:
    print("you need to pick yes or no")

print()
print(f"You chose {answer}!")
