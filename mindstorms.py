import turtle


def draw_square(some_turtle, side_length):
    for i in range(0, 4):
        some_turtle.forward(side_length)
        some_turtle.right(90)


def draw_semicircle(some_turtle, radius):
    some_turtle.circle(radius, 180)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("#003236")

    donatello = turtle.Turtle()
    donatello.hideturtle()
    donatello.color("#6FB989")
    donatello.speed(200)

    raphael = turtle.Turtle()
    raphael.hideturtle()
    raphael.color("#66A5AD")
    raphael.speed(200)

    leonardo = turtle.Turtle()
    leonardo.hideturtle()
    leonardo.color("#FB6542")
    leonardo.speed(200)

    for i in range(0, 36):
        draw_square(leonardo, 80)
        leonardo.right(10)
        draw_square(donatello, 120)
        donatello.right(10)
        draw_square(raphael, 160)
        raphael.right(10)

    window.exitonclick()


draw_art()
