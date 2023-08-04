from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(4, 1)
        self.goto(-360 * (1 if player_number == 1 else -1), 0)
        self.player_number = player_number

    def move(self, key):
        match key:
            case "w" | "up":
                if self.ycor() < 250:
                    self.goto(self.xcor(), self.ycor() + 20)
            case "s" | "down":
                if self.ycor() > -250:
                    self.goto(self.xcor(), self.ycor() - 20)
