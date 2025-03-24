from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(self.window, width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score = Label(self.window, text="Score:", bg=THEME_COLOR, borderwidth=0, highlightthickness=0)
        self.score.grid(row=0, column=1)
        self.quote = self.canvas.create_text(150, 125, width=280, text="Test!", fill='black', font=('Arial', 20, 'italic'))
        tick_img = PhotoImage(file='images/true.png')
        cross_img = PhotoImage(file='images/false.png')
        self.tick = Button(self.window, image=tick_img, borderwidth=0, highlightthickness=0, command=self.true_pressed)
        self.tick.grid(row=3, column=0)
        self.cross = Button(self.window, image=cross_img, borderwidth=0, highlightthickness=0, command=self.false_pressed)
        self.cross.grid(row=3, column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote, text=q_text)
        else:
            self.canvas.itemconfig(self.quote, text="You reached the end of the quiz")
            self.tick.config(state=DISABLED)
            self.cross.config(state=DISABLED)
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)