from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        # (x , y)
        self.direction = (-1, 0.5)

    def reset(self):
        self.goto(0, 0)

    def move(self):
        self.goto(self.direction[0] * 5 + self.xcor(), self.direction[1] * 5 + self.ycor())

    def check_collision(self):
        if abs(self.ycor()) > 290:
            self.direction = (self.direction[0], self.direction[1] * -1)

    def check_goal(self):
        if abs(self.xcor()) > 390:
            scoring_player = 1 if self.direction[0] > 0 else 2
            self.reset_ball(scoring_player)
            return scoring_player
        else:
            return False

    def paddle_hit(self):
        self.direction = (self.direction[0] * -1, self.direction[1])

    def reset_ball(self, scoring_player):
        self.goto(0, 0)
        server = -1 if scoring_player == 1 else 1
        self.direction = (-1 * server, 0.5)
