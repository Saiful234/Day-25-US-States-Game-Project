import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_file = pandas.read_csv("50_states.csv")
answer = state_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in answer if state not in guessed_states]
        # for state in answer:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed states.csv")
        break

    if answer_state in answer:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state_file[state_file.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



