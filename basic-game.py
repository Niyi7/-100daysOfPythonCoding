import turtle as t
import os

player_a_score = 0
player_b_score = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Create the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Create the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Create the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Horizontal speed
ball.dy = -2  # Vertical speed

# Create a pen for the score
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))


# Function to move the left paddle up
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)


# Function to move the left paddle down
def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)


# Function to move the right paddle up
def rightpaddleup():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)


# Function to move the right paddle down
def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)


# Assign keys for paddle movement
window.listen()
window.onkeypress(leftpaddleup, "w")
window.onkeypress(leftpaddledown, "s")
window.onkeypress(rightpaddleup, "Up")
window.onkeypress(rightpaddledown, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(player_a_score, player_b_score),
            align="center",
            font=("Arial", 24, "normal"),
        )
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(player_a_score, player_b_score),
            align="center",
            font=("Arial", 24, "normal"),
        )
        os.system("afplay wallhit.wav&")

    # Paddle and ball collisions
    if (
        (ball.dx > 0)
        and (340 < ball.xcor() < 350)
        and (rightpaddle.ycor() + 50 > ball.ycor() > rightpaddle.ycor() - 50)
    ):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

    if (
        (ball.dx < 0)
        and (-350 > ball.xcor() > -360)
        and (leftpaddle.ycor() + 50 > ball.ycor() > leftpaddle.ycor() - 50)
    ):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")
