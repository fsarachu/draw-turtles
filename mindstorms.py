import turtle


def draw_square(some_turtle, side_length):
    for i in range(0, 4):
        some_turtle.forward(side_length)
        some_turtle.right(90)


def draw_triangle(some_turtle, side_length):
    for i in range(0, 3):
        some_turtle.forward(side_length)
        some_turtle.right(120)


def draw_semicircle(some_turtle, radius):
    some_turtle.circle(radius, 180)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("#FFFFFF")

    leonardo = turtle.Turtle()
    leonardo.hideturtle()
    leonardo.color("#333333")
    leonardo.pensize(2)
    leonardo.speed(0)

    donatello = turtle.Turtle()
    donatello.hideturtle()
    donatello.color("#333333")
    donatello.pensize(2)
    donatello.speed(0)

    raphael = turtle.Turtle()
    raphael.hideturtle()
    raphael.color("#333333")
    raphael.pensize(2)
    raphael.speed(0)

    for i in range(0, 36):
        draw_square(leonardo, 80)
        leonardo.right(10)
        draw_triangle(donatello, 280)
        donatello.right(10)
        raphael.circle(120)
        raphael.right(10)

    window.exitonclick()


draw_art()
