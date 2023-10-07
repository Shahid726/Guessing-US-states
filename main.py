import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(800,800)
screen.title('United States')
image = "C:/Users/shahid/OneDrive/Desktop/programs/US_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("C:/Users/shahid/OneDrive/Desktop/programs/US_States/50_states.csv")

all_states = data.state.to_list()

# print(state_list)


guessed_states = []
score = 0
while len(guessed_states) < 50:
    answer = screen.textinput(title = f'guess the state: {score}/50', prompt = 'what is the state?').title()

    if answer == 'Exit':
        break
    
    if answer in all_states:
        all_states.remove(answer)
        guessed_states.append(answer)
        score += 1
        name_turtle = turtle.Turtle()
        state_data = data[data.state == answer]
        name_turtle.penup()
        state_coordinates = (state_data.x,state_data.y)
        name_turtle.hideturtle()
        name_turtle.goto(int(state_data.x),int(state_data.y))
        # writing the name of the state and only the name and not the extra things
        # for that we use item() method
        name_turtle.write(state_data.state.item())


un_guessed_states = []
states_x_coor = []
states_y_coor = []
for states in all_states:
    if states not in guessed_states:
        un_guessed_states.append(states)
        state_data = data[data.state == states]
        states_x_coor.append(state_data.x.item())
        states_y_coor.append(state_data.y.item())

   
data_frame = pd.DataFrame({'state':un_guessed_states,'x':states_x_coor,'y':states_y_coor})
data_frame.to_csv('missed_states.csv')










turtle.mainloop()








# screen.exitonclick()