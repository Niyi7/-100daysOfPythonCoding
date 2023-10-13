from turtle import Turtle, Screen

screen = Screen()
paddle_left = Turtle()
paddle_right = Turtle()

screen.title("My paddle_left Game")
screen.bgcolor("AliceBlue")
screen.setup(800, 600)
paddle_left.color("AliceBlue")
paddle_left.penup()
paddle_left.speed(0)
paddle_left.setpos(-350, 0)
paddle_left.shape("square")
# paddle_left.left(90)
paddle_left.shapesize(5, 1)

paddle_right.penup()
paddle_right.speed(0)
paddle_right.setpos(350, 0)
paddle_right.shape("square")
# paddle_right.left(90)
paddle_right.shapesize(5, 1)


# move = ["Up", "Down"]
# def move_right_paddle():
#     if move == "Up":
#         paddle_right.fd(50)
#     elif move == "Down":
#         paddle_right.backward(50)
def move_right_paddle_up():
    # paddle_right.fd(50)
    new_cor = paddle_right.ycor() + 20
    paddle_right.goto(paddle_right.xcor(), new_cor)


def move_right_paddle_down():
    # paddle_right.bk(50)
    new_cor = paddle_right.ycor() - 20
    paddle_right.goto(paddle_right.xcor(), new_cor)


def move_left_paddle_up():
    # paddle_left.fd(50)
    new_cor = paddle_left.ycor() + 20
    paddle_left.goto(paddle_left.xcor(), new_cor)


def move_left_paddle_down():
    # paddle_left.bk(50)
    new_cor = paddle_left.ycor() - 20
    paddle_left.goto(paddle_left.xcor(), new_cor)


# def move_up():
#     paddle_right.fd(50)


screen.listen()
screen.onkey(move_right_paddle_up, "Up")
screen.onkey(move_right_paddle_down, "Down")
screen.onkey(move_left_paddle_up, "w")
screen.onkey(move_left_paddle_down, "s")


screen.exitonclick()
