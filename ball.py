import turtle


class Bal(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.direction_x = 10
        self.direction_y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.direction_x
        y = self.ycor() + self.direction_y
        self.goto(x, y)

    def bounce_y(self):
        self.direction_y *= -1

    def bounce_x(self):
        self.direction_x *= -1

    def round(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

    def faster(self):
        if self.move_speed > 0.02:
            self.move_speed -= 0.01
