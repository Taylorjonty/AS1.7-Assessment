# Similar to
def yes_no(question_text):
    while True:

        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please answer 'yes' or 'no'")


show_instruction = yes_no("Have you played this game before: ")
print(f"You entered {show_instruction}")
