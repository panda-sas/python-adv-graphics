import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Tell a state's name?").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if answer_state == "Exit":

        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_match = data[data.state == answer_state]
        t.goto(int(state_match.x), int(state_match.y))
        t.write(answer_state)


# obtain mouse click coordinates
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# # onscreenclick is an event listener
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()
