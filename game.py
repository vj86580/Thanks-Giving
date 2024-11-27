
import turtle
import random
import grid

# Creating Game Screen
screen = grid.screen
#screen.register_shape()
screen.register_shape("images/1.gif")
screen.register_shape("images/2.gif")
#screen.register_shape("images/2.png")
screen.register_shape("images/3.gif")
screen.register_shape("images/4.gif")
screen.register_shape("images/basket.gif")


# Create Shape
def create_shape(x, y, img="square.png", screen=screen):
    img = "images/{image}".format(image=img)
    #screen.register_shape(img)
    shape = turtle.Turtle()
    shape.penup()
    shape.goto(x, y)
    shape.shape(img)
    return shape


# Move functions
def move_left(shape, speed):
    x = shape.xcor() - speed
    y = shape.ycor()
    shape.goto(x, y)


def move_right(shape, speed):
    x = shape.xcor() + speed
    y = shape.ycor()
    shape.goto(x, y)


def move_up(shape, speed):
    x = shape.xcor()
    y = shape.ycor() + speed
    shape.goto(x, y)


def move_down(shape, speed):
    x = shape.xcor()
    y = shape.ycor() - speed
    shape.goto(x, y)


# Add background to the game
def add_background(img="bg.png", screen=screen):
    img = "images/{image}".format(image=img)
    screen.bgpic(img)


def reset(shape):
    if shape.ycor() < -270:
        shape.speed(0)
        shape.goto(random.randint(-130, 130), 270)
        food = random.randint(1, 4)
        shape.shape("images/" + str(food) + ".gif")
        #shape.showturtle()


def hide(shape):
    shape.speed(0)
    shape.goto(random.randint(-130, 130), 270)
    food = random.randint(1, 4)
    shape.shape("images/" + str(food) + ".gif")


def title_turtle():
    title_turt = turtle.Turtle()
    title_turt.penup()
    title_turt.goto(-180, 270)
    title_turt.color("white")
    title_turt.hideturtle()
    return title_turt


title_turt = title_turtle()


def game_title(text, title_turt=title_turt):
    title_turt.write(text, font=("Arial", 15, "bold"))


def track_asteroid(objectA, objectB):
    distance = objectA.distance(objectB)
    start = -35
    end = 35
    return distance > start and distance < end and distance > 0


def dodge_asteroid(spaceship, asteroid):
    distance = spaceship.distance(asteroid)
    if ((distance > 0) and (-120 <= spaceship.xcor() <= 0)):
        move_left(spaceship, 30)
    elif ((distance > 0) and (-200 <= spaceship.xcor() < -120)):
        move_right(spaceship, 200)
    elif ((distance > 0) and (0 < spaceship.xcor() <= 120)):
        move_left(spaceship, 30)
    elif ((distance > 0) and (120 < spaceship.xcor() <= 200)):
        move_right(spaceship, 200)

import main
def setup_keybindings():
    screen.listen()
    screen.onkey(lambda: move_left(main.spaceship, 20), "Left")
    screen.onkey(lambda: move_right(main.spaceship, 20), "Right")
    screen.onkey(lambda: move_up(main.spaceship, 20), "Up")
    screen.onkey(lambda: move_down(main.spaceship, 20), "Down")


# Add background and update game loop
def run_game():
    screen.tracer(0)  # Disable automatic updates to control frame rate
    while True:
        main.game_loop()
        add_background("bg.png")  # Add background on every loop iteration
        screen.update()  # Update the screen after the game logic


# Set up keybindings before the game loop
setup_keybindings()

# Start the game
run_game()
screen.listen()
screen.onkey(lambda: move_left(spaceship, 10), "Left")
screen.onkey(lambda: move_right(spaceship, 10), "Right")
screen.onkey(lambda: move_up(spaceship, 10), "Up")
screen.onkey(lambda: move_down(spaceship, 10), "Down")
