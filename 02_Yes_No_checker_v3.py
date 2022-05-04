# Similar to 02_yes_no_checker_v2
# turned it into a function to copy to the base code

def yes_no(question_text):
    while True:
        # Ask if the person has played before
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


show_instruction = yes_no("Have you played this game before: ")

