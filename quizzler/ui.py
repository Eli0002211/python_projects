from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("arial", 20, "italic")

class Quiz_Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.rowconfigure(2, minsize= 120)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 150, text="", font=FONT, fill=THEME_COLOR ,width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file=r".\images\true.png")
        self.true_button = Button(image=self.true_img, command=self.answer_true, pady=50, padx=50,  highlightcolor=THEME_COLOR, bg=THEME_COLOR)
        self.true_button.grid(row=2,column=0)

        self.false_img = PhotoImage(file=r".\images\false.png")
        self.false_button = Button(image=self.false_img, command=self.answer_false, pady=50, padx=50, highlightcolor=THEME_COLOR, bg=THEME_COLOR)
        self.false_button.grid(row=2,column=1)

        self.score_count = Canvas(width=120, height=50, bg=THEME_COLOR, highlightthickness=0)
        self.score_count_text = self.score_count.create_text(50, 10, text=f"Score: {self.quiz.score}", fill="#FFFFFF", font=FONT)
        self.score_count.grid(row=0, column=1)
        self.get_next_question()
        self.window.mainloop()

    def answer_true(self):

        self.outcome = self.quiz.check_answer(user_answer="true")
        self.update_score(self.outcome)


    def answer_false(self):

        self.outcome = self.quiz.check_answer(user_answer="false")
        self.update_score(self.outcome)


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_count.itemconfig(self.score_count_text, text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="#FFFFFF")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="#FFFFFF")
            q_text = f"You have answered all questions! Your final score is {self.quiz.score}/10!"
            self.canvas.itemconfig(self.question, text=q_text)
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")


    def update_score(self, outcome):
        if outcome:

            self.canvas.config(bg="#66ff00")
        else:

            self.canvas.config(bg="#EE4B2B")
        self.window.after(1000, self.get_next_question)





