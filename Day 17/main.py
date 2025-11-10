from question_model import Question
from data import question_data
from quiz_brain import Quiz
from os import system

question_bank = []


for question in question_data :
    text = question["question"]
    ans = question["correct_answer"]
    new_obj = Question(text,ans)
    question_bank.append(new_obj)

quiz = Quiz(question_bank=question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

system("cls")
print("\n\nYou complete the quiz")
print(f"your score is : {quiz.score} / {quiz.question_number}")