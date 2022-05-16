# This component will be at the very start of the game. it will also check if the player is in primary school
# based off 01_age_checker_v2 but this time in a function

def age_checker():


# main routine
age_checker()
def yes_no(question_text):
    while True:

        answer = input(question_text ).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please answer 'yes' or 'no'")

show_instruction = yes_no("Have you played this game before? ")
print(f"You entered {show_instruction}")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered {show_instruction}")
