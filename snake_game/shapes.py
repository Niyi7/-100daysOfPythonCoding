from turtle import Screen, Turtle, colormode
import random

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("teal")
# screen.title("My shape Game")


# # Draw a Triangle
# shape = Turtle()
# shape.shape("square")
# shape.color("red")
# shape.shapesize(0.2, 0.2)
# shape.speed(5)
# shape.forward(200)
# shape.right(90)
# shape.forward(200)
# shape.right(135)
# shape.forward(283)

# # Draw a Square
# shape.shape("turtle")
# shape.color("black")
# shape.left(45)
# shape.forward(100)
# for _ in range(3):
#     shape.right(90)
#     shape.forward(200)
# shape.right(90)
# shape.forward(100)

# shape.clear()

# # Create Dashed lines
# for _ in range(10):
#     shape.forward(10)
#     shape.color("teal")
#     shape.forward(10)
#     shape.color("black")

# # Create Dashed Lines - Angela Yu's solution
# for _ in range(3):
#     shape.right(90)
#     for _ in range(10):
#         shape.forward(10)
#         shape.penup()
#         shape.forward(10)
#         shape.pendown()
# screen.clear()


# # Shapes - Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon and Decagon. -- Divide 360 by total number of sides to find their degrees.

# screen = Screen()
# screen.setup(width=600, height=600)
# # screen.bgcolor("aqua")
# screen.title("My shape Game")

# shape = Turtle()
# shape.penup()
# shape.goto(-50, 150)
# shape.pendown()
# shape.shape("turtle")
# shape.width(3)
# shape.shapesize(0.2, 0.2)
# shape.speed(5)
# colormode(255)


# pace = 100
# sides = 3


# for _ in range(8):
#     degree = 360 / sides
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     for _ in range(sides):
#         tup = (r, g, b)
#         shape.color(tup)
#         shape.forward(pace)
#         shape.right(degree)
#     # pace += 10
#     sides += 1


# shape.clear()


# Angela's Solution

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
colors.remove("wheat")
print(colors)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         shape.forward(100)
#         shape.right(angle)


# for shape_side_n in range(3, 11):
#     shape.color(random.choice(colors))
#     draw_shape(shape_side_n)


# screen.exitonclick()
