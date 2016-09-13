import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("#50CC99")

    donatello = turtle.Turtle()
    donatello.shape("turtle")
    donatello.color("#209C69")
    donatello.pensize(3)

    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)
    donatello.right(180)

    donatello.circle(25, 180)
    donatello.right(180)
    donatello.circle(25, 180)
    donatello.right(180)
    donatello.circle(25, 180)
    donatello.right(180)
    donatello.circle(25, 180)

    window.exitonclick()


draw_square()
