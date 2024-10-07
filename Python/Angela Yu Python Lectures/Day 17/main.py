from data import *
from question_class import *
from quiz_brain import *

if __name__ == "__main__":
    my_question_bank = []
    for question in question_data:
        text = question["text"]
        answer = question["answer"]
        my_question_bank.append(Questions(question_t=text, answer_t=answer))
    
    quiz_brain(my_question_bank)
        