import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
img = "D:\Documents/Haikal/Python\day 25 working CSV data and pandas library/us-states-game/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv("D:\Documents/Haikal/Python\day 25 working CSV data and pandas library/us-states-game/50_states.csv")
all_states = data.state.to_list()
guess_states = []


while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Guess the State", prompt="What's another state's name?").title()


    if answer_state == "Exit":
        misssing_state = []
        for state in all_states:
            if state not in guess_states:
                misssing_state.append(state)
        new_data = pandas.DataFrame(misssing_state)
        new_data.to_csv("states_to_learn.csv")
        break
     
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

