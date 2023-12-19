import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Courier", 80, "bold"))

    def win_right(self):
        self.right_score += 1
        self.update()

    def win_left(self):
        self.left_score += 1
        self.update()
