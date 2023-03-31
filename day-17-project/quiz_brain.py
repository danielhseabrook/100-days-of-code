import time
from os import system
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        for question in self.question_list:
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}:{current_question.text}(True/False)\n")
            self.check_answer(answer, current_question.answer)
            #time.sleep(5)
            #system('clear')
        print(f"Your final score is: {self.score}/{self.question_number}")

    def check_answer(self, user, actual):
        if user.lower() == actual.lower():
            self.score += 1
            print(f"Correct!\nYour current score is: {self.score}")
        else:
            print(f"Incorrect! The correct answer was {actual}.\n"
                  f"Your current score is {self.score}/{self.question_number}")