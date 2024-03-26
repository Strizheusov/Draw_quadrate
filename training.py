import turtle
def move(q):
    turtle.forward(q)
    turtle.left(90)
def draw_square(q):
    for i in range(4):
        move(q)

def draw_squarecollor(q,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        move(q)
    turtle.end_fill()
turtle.speed(1)
draw_squarecollor(80, 'red')
turtle.goto(150, 150)
draw_squarecollor(120, 'blue')

