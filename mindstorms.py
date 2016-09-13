import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    donatello = turtle.Turtle()
    donatello.forward(100)

    window.exitonclick()


draw_square()
