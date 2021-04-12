import turtle as t
import time
import random

snake = [] # List of object turtle
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to the Snake's Den")
score = t.Turtle() # Turtle made to maintain the scoreboard
score.color('White')
score.penup()
score.hideturtle()
score.goto(0, 270)
sc = 0

if sc == 0:
    score.write(f"Score : {sc} ", align='center', font=('Courier', 22, 'normal'))

# Increasing the score after every collision with Food
def sc_inc():
    score.clear()
    global sc
    sc += 1
    score.write(f"Score : {sc} ", align='center', font=('Courier', 22, 'normal'))


screen.tracer(0) # Used to make the activities unseen and when update is called , the final result is displayed
for i in range(3):
    tim = t.Turtle()
    tim.speed('slow')
    tim.setx(-20 + 20 * i)
    tim.shape('square')
    tim.color('white')
    snake.append(tim)
h = len(snake)
'''game_on = True'''
snake[h-1].penup()  # h-1 as we are incrementing on the first position of the List making h-1 the head.

# Direction control using keys and if a turtle goes in one direction, It can't go on the opposite direction
def right():
    if snake[h - 1].heading() != 180:
        snake[h-1].setheading(0)


def up():
    if snake[h-1].heading() != 270:
        snake[h-1].setheading(90)


def left():
    if snake[h - 1].heading() != 0:
        snake[h-1].setheading(180)


def down():
    if snake[h-1].heading() != 90:
        snake[h-1].setheading(270)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(down, "Down")
# Food made using another turtle and is placed at a random position in the screen
food = t.Turtle()
food.penup()

# Function to randomly get the position where the food is placed


def ref():
    xxx = random.randint(-280, 280)
    yyy = random.randint(-280, 280)
    for i in snake:
        if food.pos() == i.pos():
            break
    food.goto(xxx, yyy)


food.shape('circle')
food.color('green')
food.shapesize(0.5)

ref()
# main game logic
game_on = True
while game_on:
    screen.update() # The update happens once the central turtles are created
    time.sleep(0.1)
    for hiss in range(h - 1):
        snake[hiss].speed('slow')
        snake[hiss].penup()
        # we are moving the last element of the list to the 2nd last to make the turtle move
        new_x = snake[hiss + 1].xcor()
        new_y = snake[hiss + 1].ycor()

        snake[hiss].goto(new_x, new_y)
    # After the second element of the list goes to the first
    # The first element can't go to h-1 thus we move it forward after the loop
    snake[h - 1].forward(20)

    # Detecting collision with food with a gap between the turtle obj and food <17
    if snake[h - 1].distance(food) < 17:
        ref()
        new_tim = t.Turtle()
        new_tim.penup()
        new_tim.shape('square')
        new_tim.color('white')
        # The new turtle object has to go to the start of the list as that is the tail
        new_tim.goto((snake[0].xcor()), (snake[0].ycor()))
        snake.insert(0, new_tim)
        h += 1
        # IF this is true, then we increment the score
        sc_inc()
    # Detect collision with walls and print GAME OVER at center
    if snake[h-1].xcor() > 290 or snake[h-1].xcor() < -300 or snake[h-1].ycor() > 300 or snake[h-1].ycor() < -290:
        score.goto(0, 0)
        score.write(f"GAME OVER", align='center', font=('Courier', 22, 'normal'))
        game_on = False
    # Detect collision with snake body
    for i in range(1, h - 1):
        if snake[h-1].distance(snake[i]) < 10:
            score.goto(0, 0)
            score.write(f"GAME OVER", align='center', font=('Courier', 22, 'normal'))
            game_on = False
screen.exitonclick()