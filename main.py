import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

t.goto(0, 250)
t.write("Type exit to quit the game", align="center", font=("Arial", 16, "bold"))

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What's the name of the "
                                                                                              "state?").title()
    if answer_state == "Exit":

        missed_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)

        # df = pandas.DataFrame(missed_states)
        # df.to_csv("Missed_States.csv")

        with open("learn.txt", mode="w") as file:
            for state in missed_states:
                file.write(f"{state}\n")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Arial", 10, "bold"))

turtle.mainloop()
