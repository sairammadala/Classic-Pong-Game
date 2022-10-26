from turtle import *

frame = Screen()

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle = []
        self.up = 0

    def create_paddle(self, i, side):
        t = Turtle()
        t.shape("square")
        if side == -1:
            t.color("red")
        elif side == 1:
            t.color("blue")
        t.setheading(90)
        t.speed("fastest")
        t.penup()
        t.shapesize(stretch_len=0.5, stretch_wid=0.5)
        t.goto(side * 285, -20 + i * 10)
        self.paddle.append(t)

    def down_movement(self):
        self.paddle[0].setheading(270)
        for i in range(len(self.paddle) - 1, 0, -1):
            self.pos = self.paddle[i - 1].pos()
            self.paddle[i].goto(self.pos)

    def up_movement(self):
        for i in range(0, len(self.paddle) - 1):
            self.pos = self.paddle[i + 1].pos()
            self.paddle[i].goto(self.pos)

    def motion(self, up):
        if up == 1:
            self.up_movement()
            self.paddle[-1].fd(10)
        elif up == -1:
            self.down_movement()
            self.paddle[0].fd(10)
        return self.check_game()

    def upwards(self):
        self.up = 1

    def downwards(self):
        self.up = -1

    def check_game(self):
        self.y1 = self.paddle[0].ycor()
        self.y2 = self.paddle[-1].ycor()
        if self.y1 < -290 or self.y2 > 290:
            return False
        return True
