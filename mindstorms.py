import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("#50CC99")

    # Draw square
    donatello = turtle.Turtle()
    donatello.shape("turtle")
    donatello.color("#209C69")
    donatello.pensize(3)
    donatello.speed(1.7)

    for i in range(0, 4):
        donatello.forward(200)
        donatello.right(90)

    # Draw semicircles
    raphael = turtle.Turtle()

    raphael.shape("turtle")
    raphael.color("#209C69")
    raphael.pensize(2)
    raphael.speed(6)

    raphael.right(90)

    for i in range(0, 4):
        raphael.circle(25, 180)
        raphael.right(180)

    window.exitonclick()


draw_square()
