from turtle import Screen
import time
from snake import Snake

# Screen Setup
screen = Screen()
screen.bgcolor("teal")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")

screen.exitonclick()
