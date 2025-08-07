
class Quiz:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0


    def still_has_questions(self) :
        return self.question_number < len(self.question_list)

    def next_question(self):
        ans = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number } {ans.text} (True/False) :")
        self.check_ans(user_ans,ans.answer)


    def check_ans(self,user_ans,ans):
        if user_ans.lower() == ans.lower() :
            print("you got it !")
            self.score += 1
        else:
            print("you are wrong")
        print(f"correct ans is {ans}")
        print(f"score is : {self.score}/{self.question_number}\n")

