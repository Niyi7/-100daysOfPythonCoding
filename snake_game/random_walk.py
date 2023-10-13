from turtle import Screen, Turtle, colormode
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.title("A Random Walk")

walk = Turtle()
random_width = random.randint(5, 15)
rand_dir = [0, 90, 180, 270]
colormode(255)
walk.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


for steps in range(100):
    walk.width(random_width)
    walk.color(random_color())
    walk.forward(30)
    walk.setheading(random.choice(rand_dir))

walk.clear()
walk.penup()
walk.home()
walk.pendown()
walk.width(1)

# Draw a Spirograph
for _ in range(100):
    walk.color(random_color())
    walk.circle(100)
    walk.left(10)

walk.clear()
walk.penup()
walk.home()
walk.pendown()


# Angela Yu's Solution
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        walk.color(random_color())
        walk.circle(100)
        walk.setheading(walk.heading() + size_of_gap)


draw_spirograph(10)


# Beautiful Patterns
# for steps in range(100):
#     for c in ("blue", "red", "green"):
#         walk.color(c)
#         walk.forward(steps)
#         walk.right(35)


screen.exitonclick()
