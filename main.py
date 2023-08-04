from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
player_one = Paddle(1)
player_two = Paddle(2)

ball = Ball()
screen.listen()
screen.onkeypress(lambda: player_one.move("w"), "w")
screen.onkeypress(lambda: player_one.move("s"), "s")
screen.onkeypress(lambda: player_two.move("up"), "Up")
screen.onkeypress(lambda: player_two.move("down"), "Down")
while True:
    ball.move()
    ball.check_collision()
    scoring_player = ball.check_goal()
    if scoring_player:
        scoreboard.increase_score(scoring_player)
    if abs(player_one.xcor() - ball.xcor()) < 20 and abs(player_one.ycor() - ball.ycor()) < 50 \
            or abs(player_two.xcor() - ball.xcor() < 20) and abs(player_two.ycor() - ball.ycor()) < 60:
        ball.paddle_hit()
    screen.update()
    time.sleep(0.01)


screen.exitonclick()
