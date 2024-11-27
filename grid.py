import turtle

screen = turtle.Screen()
screen.setup(400, 600)
screen.bgcolor('gray')

grid = turtle.Turtle()
grid.color("dark gray")

turtle.speed(0)

grid.speed(0)
grid.penup()
grid.goto(-300,0)
grid.pendown()
grid.right(90)

def grid1():
    for i in range(-300, 300, 20):
        grid.penup()
        grid.goto(i, 300)
        grid.pendown()
        grid.forward(600)
        
    grid.left(90)
        
    for j in range(-300, 300, 20):
        grid.penup()
        grid.goto(-300, j)
        grid.pendown()
        grid.forward(600)
        
    #x axis
    grid.penup()
    grid.goto(-300, 0)
    grid.pendown()
    grid.pensize(4)
    grid.forward(600)
    
    #y axis
    grid.penup()
    grid.goto(0, 300)
    grid.right(90)
    grid.pendown()
    grid.pensize(3)
    grid.forward(600)

def dragging(x, y): 
    print(round(x/20) * 20, round(y/20) * 20)

#grid1()
grid.left(90)

screen.listen()
screen.onscreenclick(dragging, 3)

turtle.hideturtle()
