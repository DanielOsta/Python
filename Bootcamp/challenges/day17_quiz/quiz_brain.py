class QuizBrain:
    def __init__(self, q_list):
        self.question_numer = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_numer < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_numer]
        self.question_numer += 1
        input(f"Q.{self.question_numer} {current_question.text} (True/False)?: ")
