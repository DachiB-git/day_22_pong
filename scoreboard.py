from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_one_score = 0
        self.player_one_counter = self.generate_counter(-200, self.player_one_score)
        self.player_two_score = 0
        self.player_two_counter = self.generate_counter(200, self.player_two_score)
        self.generate_divider()

    @staticmethod
    def generate_divider():
        divider = Turtle()
        divider.color("white")
        divider.hideturtle()
        divider.penup()
        divider.goto(0, 300)
        divider.setheading(270)
        for _ in range(20):
            divider.pendown()
            divider.forward(20)
            divider.penup()
            divider.forward(10)
    @staticmethod
    def generate_counter(x_cord, player_score):
        score = Turtle()
        score.penup()
        score.hideturtle()
        score.color("white")
        score.goto(x_cord, 230)
        score.write(player_score, align="center", font=("Aria", 30, "normal"))
        return score

    def update_score(self, counter):
        if counter == 1:
            self.player_one_counter.clear()
            self.player_one_counter.goto(-200, 230)
            self.player_one_counter.write(self.player_one_score, align="center", font=("Aria", 30, "normal"))
        else:
            self.player_two_counter.clear()
            self.player_two_counter.goto(200, 230)
            self.player_two_counter.write(self.player_two_score, align="center", font=("Aria", 30, "normal"))


    def increase_score(self, player):
        if player == 1:
            self.player_one_score += 1
            self.update_score(1)
        else:
            self.player_two_score += 1
            self.update_score(2)
