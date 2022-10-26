from paddle import *
from time import *
from ball import *
from scoreboard import *

frame = Screen()
frame.setup(width=600, height=600)
frame.bgcolor("yellow")
frame.listen()


left_paddle = Paddle()
right_paddle = Paddle()


#key events

frame.onkey(left_paddle.upwards, "w")
frame.onkey(left_paddle.downwards, "s")
frame.onkey(right_paddle.upwards, "Up")
frame.onkey(right_paddle.downwards, "Down")


frame.tracer(0)

for segment in range(5):
  left_paddle.create_paddle(segment, -1)
  right_paddle.create_paddle(segment, 1)


Total_paddles = [left_paddle, right_paddle]
score = Score()
ball = Ball()


frame.update()
game_on= True
while game_on:
  frame.update()
  sleep(0.075)
  l_game_on = left_paddle.motion(left_paddle.up)
  r_game_on = right_paddle.motion(right_paddle.up)
  b_game_on = ball.ball_movement(Total_paddles)
  score.updated_score(ball.left_paddle_hits, ball.right_paddle_hits)
  if not (l_game_on and r_game_on and b_game_on):
    game_on = False

game = Turtle()
game.color("red")
game.hideturtle()
game.write("GAME OVER!!!", align="center", font=("arial", 24, "normal"))


frame.exitonclick()
