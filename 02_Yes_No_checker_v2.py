# This component is based on 02_Yes_no_checker_v1. We are making it will loop until we want it to stop
# it will also allow you to enter Y or N now
answer = ""

while answer != "x":
    # Ask the player if they have played before
    answer = input("Have you played the game before: ").lower()
    # if the answer is yes, start the game.
    if answer == "yes":
        print("program continues")
    # if the answer is no, show the instructions
    elif answer == "no":
        print("*** Instructions ***")
    # Tells the player that they need to answer only yes or no
    else:
        print("you need to pick yes or no")

    print(f"You chose {answer}!")
    print()
