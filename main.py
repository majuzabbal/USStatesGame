import turtle
import pandas

tur = turtle.Turtle()
tur.penup()
tur.hideturtle()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []
game_is_on = 0
while game_is_on < 50:
    answer_state = screen.textinput(title=f"{game_is_on}/50 States", prompt="What's another state name?")
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)

        print(missing_states)
        break

    if answer_state in states:
        state_data = data[data.state == answer_state]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(answer_state)

        guessed_states.append(answer_state)
        game_is_on += 1

