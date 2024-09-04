from question_class import *
def quiz_brain(my_question_bank):
    for question in my_question_bank:
        answer = input(question.question + "(True/False): ")
        if answer == question.answer:
            print("Correct answer\n")
        else:
            print("Wrong answer\n")