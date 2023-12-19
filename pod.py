import turtle


class Pod(turtle.Turtle):

    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()
        self.goto(coord)

    def up(self):
        y = self.ycor()
        if y < 260:
            y += 40
            self.sety(y)
            self.screen.update()
        else:
            return False

    def down(self):
        y = self.ycor()
        if y > -260:
            y -= 40
            self.sety(y)
            self.screen.update()
        else:
            return False
