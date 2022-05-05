# Similar to 02_yes_no_checker_v2
# I have turned it into a function to copy to the base code

def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        # If the answer is yes, continue
        if answer == "yes" or answer == "y":
            answer = "Yes"
            print("continue code")
            return answer
        # If the answer is no, show the instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            print("instructions")
            return answer
        # Tell player to answer yes or no
        else:
            print("Please answer 'yes' or 'no'")


# Ask if the person has played before
show_instruction = yes_no("Have you played this game before: ")

