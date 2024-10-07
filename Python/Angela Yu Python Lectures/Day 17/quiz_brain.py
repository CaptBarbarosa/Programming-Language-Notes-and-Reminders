from question_class import *
def quiz_brain(my_question_bank):
    true = 0
    wrong = 0
    for question in my_question_bank:
        answer = input(question.question + "(True/False): ")
        if answer == question.answer:
            print("Correct answer\n")
            true += 1 
        else:
            print("Wrong answer\n")
            wrong += 1
    print("You got ",true, "out of ",(true+wrong)," Correct while ",wrong," out of ",(true+wrong)," wrong")