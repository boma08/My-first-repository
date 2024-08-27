from turtle import Turtle, Screen
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
screen = Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

states_data_frame = pandas.read_csv("50_states.csv")
all_states = states_data_frame.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                   prompt="Whats the name of another state? ").title()
    if user_answer == "Exit":
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data_frame[states_data_frame.state == user_answer]
        x_coor = int(state_data.x)
        y_coor = int(state_data.y)
        t.goto(x_coor, y_coor)
        t.write(user_answer)

states_to_learn = [state for state in all_states if state not in guessed_states]  # replaces the 3 lines below
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")


screen.exitonclick()


