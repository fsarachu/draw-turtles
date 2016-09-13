import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

    donatello = turtle.Turtle()

    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)
    donatello.right(90)
    donatello.forward(200)

    window.exitonclick()


draw_square()
