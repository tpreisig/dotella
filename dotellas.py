import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def draw_dotellas():
    dotella = Turtle()
    dotella.hideturtle()
    dotella.speed("fastest")

    def rand_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)

    screen = Screen()
    bg_c = ["cbd7ef","#fdfd99", "#b5cae8","#de779d", "#86c192", "#fd9e15", "#c6fff9", "#b5cae8", "#bf93fd", "#b4fda7", "#fae291",
                   "#bf93fd", "#dfe1e5", "#efbce7", "#c5e5ff","#F8E8EE", "#F9F5F6", "#FFF1DC", "#FFDEB4", "#A7ECEE", "#FDCEDF", "#FBFFDC", "#D0F5BE", "#BCCEF8"]
    chosen_color = random.choice(bg_c)
    screen.bgcolor(chosen_color)

    doty = 250
    dotx = -275

    for d in range(13):
        dotella.penup()
        dotella.sety(doty)
        dotella.setx(dotx)
        for _ in range(15):
            dotella.dot(random.randint(25,39), rand_color())
            dotella.penup()
            dotella.forward(40)
            dotella.pendown()
        dotella.penup()
        doty -= 40
        dotella.backward(360)
        dotella.pendown()
        
    screen.mainloop()


draw_dotellas()
        
