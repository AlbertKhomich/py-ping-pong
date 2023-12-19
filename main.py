import turtle
import pod
import ball
import time
import scoreboard

game_on = True

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pod_left = pod.Pod((-350, 0))
pod_right = pod.Pod((350, 0))
ball = ball.Bal()
scoreboard = scoreboard.Scoreboard()

screen.listen()

screen.onkey(pod_left.up, "w")
screen.onkey(pod_left.down, "s")

screen.onkey(pod_right.up, "8")
screen.onkey(pod_right.down, "2")

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    elif ball.xcor() > 330 and ball.distance(pod_right) < 50 or ball.xcor() < -330 and ball.distance(pod_left) < 50:
        ball.bounce_x()
        ball.faster()
    elif ball.xcor() > 380:
        ball.round()
        scoreboard.win_left()
    elif ball.xcor() < -380:
        ball.round()
        scoreboard.win_right()

screen.exitonclick()
