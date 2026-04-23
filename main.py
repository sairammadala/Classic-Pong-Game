from time import sleep
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Score

frame = Screen()
frame.setup(width=800, height=600)
frame.title("Classic Pong")
frame.bgcolor("#0b1020")
frame.listen()
frame.tracer(0)

left_paddle = Paddle()
right_paddle = Paddle()

# key events

frame.onkey(left_paddle.upwards, "w")
frame.onkey(left_paddle.downwards, "s")
frame.onkey(right_paddle.upwards, "Up")
frame.onkey(right_paddle.downwards, "Down")
frame.onkeyrelease(left_paddle.stop, "w")
frame.onkeyrelease(left_paddle.stop, "s")
frame.onkeyrelease(right_paddle.stop, "Up")
frame.onkeyrelease(right_paddle.stop, "Down")

for segment in range(5):
    left_paddle.create_paddle(segment, -1)
    right_paddle.create_paddle(segment, 1)

center_line = Turtle()
center_line.hideturtle()
center_line.color("#4a5572")
center_line.penup()
center_line.goto(0, 290)
center_line.setheading(270)
for _ in range(18):
    center_line.pendown()
    center_line.forward(15)
    center_line.penup()
    center_line.forward(17)

Total_paddles = [left_paddle, right_paddle]
score = Score()
ball = Ball()

frame.update()
game_on = True
while game_on:
    frame.update()
    sleep(0.055)
    left_paddle.motion(left_paddle.up)
    right_paddle.motion(right_paddle.up)
    b_game_on = ball.ball_movement(Total_paddles)
    score.updated_score(ball.left_paddle_hits, ball.right_paddle_hits)
    if not b_game_on:
        game_on = False

game = Turtle()
game.color("#f87171")
game.hideturtle()
game.write("GAME OVER", align="center", font=("Arial", 28, "bold"))

frame.exitonclick()
