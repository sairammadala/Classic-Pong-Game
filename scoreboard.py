from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#e2e8f0")
        self.penup()
        self.goto(x=0, y=260)

    def updated_score(self, left_paddle_hits, right_paddle_hits):
        self.clear()
        self.write(
            f"{left_paddle_hits}  :  {right_paddle_hits}",
            align="center",
            font=("Arial", 24, "bold"),
        )
