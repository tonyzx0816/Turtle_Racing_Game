from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet",
                            prompt = "Which turtle will win the race?"
                                     " Enter a color(red/purple/green/yellow/orange/blue): ")
color = ["red", "purple", "green", "yellow", "orange", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    t = Turtle(shape = "turtle")
    t.color(color[turtle_index])
    t.penup()
    t.goto(x = -230, y = y_position[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()