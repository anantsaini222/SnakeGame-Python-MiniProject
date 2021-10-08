# Tkinter
# Framework provides python users with a simple way
# to create GUI elements using the widgets foung in Tk toolkit
# Tk widgets can be used to construct buttons, menus, data fields etc

# To create a tkinter app:

# Importing the module – tkinter
# Create the main window (container)
# Add any number of widgets to the main window
# Apply the event Trigger on the widgets.

# Main Tkinter module.

# tkinter.colorchooser
# Dialog to let the user choose a color.

# tkinter.commondialog
# Base class for the dialogs defined in the other modules listed here.

# tkinter.filedialog
# Common dialogs to allow the user to specify a file to open or save.

# tkinter.font
# Utilities to help work with fonts.

# tkinter.messagebox
# Access to standard Tk dialog boxes.

# tkinter.scrolledtext
# Text widget with a vertical scroll bar built in.

#import packages
import turtle  #pip install turtle
import random #pip install random
import time 

# creating screen 
screen = turtle.Screen() #used to set the size and position of the main window.
screen.title("Anant's Project")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#setting footer
t = turtle.Turtle()
t.penup()
t.goto(-250,-320)
t.color('white')
style = ('Courier',25,'italic')
t.write('Anant Saini ©® flexncode',font=style,align='left')
t.hideturtle()

#creating border
turtle.speed(5)
turtle.pensize(4) #width of the border
turtle.penup()
turtle.goto(-310, 250) # postion with respect to screen X or Y value
turtle.pendown()
turtle.color("red") # color of border
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score
score = 0
delay = 0.1

#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("circle")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("white")
fruit.penup()
fruit.goto(30 , 30)

old_fruit = []

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: \n\n",align="center",font=("Courier",24,"bold"))
scoring.write("SNAKE GAME",align="center",font=("Courier",24,"bold"))

#define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"
        
def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20) 
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20) 
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20) 


#keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#main loop
while True:
    screen.update()

    # snake $ fruit colision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 10
        scoring.write("Score: {}".format(score),align="center",font=("Courier",24,"bold"))
        delay -= 0.001

        #creating new foods
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle") 
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    #adding ball to snake
    for index in range(len(old_fruit) -1, 0 ,-1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()


    #snake and border colision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0 ,0)
        scoring.write("   Game Over \n Your Score : {}".format(score),align="center",font=("Courier",30,"bold"))
        

    #snake colisons
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0 ,0)
            scoring.write("   Game Over \n Your Score : {}".format(score),align="center",font=("Courier",30,"bold"))
            
    time.sleep(delay)

turtle.Terminator()
