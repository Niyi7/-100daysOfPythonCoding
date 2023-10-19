from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scores

# Screen Setup
screen = Screen()
screen.bgcolor("teal")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scores()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.move()
        snake.increase()
        snake.move()
        score.add_score()

    # Detect collision with Walls
    if (
        snake.head.xcor() > 295
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -295
    ):
        game_is_on = False
        score.game_over()

    # Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    screen.listen()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")

screen.exitonclick()
