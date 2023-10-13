from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
states = Turtle()
screen.bgpic("blank_states_img.gif")
states.pen(shown=False)
states.penup()
states.speed(1)

data = pd.read_csv("50_states.csv")
t = 0
correct_guesses = []
state_column = data.state.to_list()
states_to_learn = []

while len(correct_guesses) < 50:
    user_input = str(
        screen.textinput(
            f" {t}/50 US States Guessed Correctly", "Guess the Blank States ☺ or type exit to leave the game",
        )
    )
    guess_name = user_input.title()
    if guess_name == "Exit":
        break
    for items in state_column:
        if guess_name == items:
            correct_guesses.append(guess_name)
            x = data[data.state == items].x
            x_cord = float(x.to_list()[0])
            y = data[data.state == items].y
            y_cord = float(y.to_list()[0])
            states.goto(x_cord, y_cord)
            states.write(guess_name, align="center")
            t += 1
        # to_learn =
    state_column.remove(guess_name)

states_to_learn.append(state_column)
state_data = pd.DataFrame(states_to_learn)
state_data.to_csv("states_to_learn.csv")
print(state_data)
# Angela's Solution

# screen.exitonclick()
