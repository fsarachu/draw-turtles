import turtle


def draw_square(some_turtle, side_length):
    for i in range(0, 4):
        some_turtle.forward(side_length)
        some_turtle.right(90)


def draw_semicircle(some_turtle, radius):
    some_turtle.circle(radius, 180)


def draw_art():
    window = turtle.Screen()

    # Draw square
    donatello = turtle.Turtle()
    draw_square(donatello, 100)

    # Draw semicircle
    raphael = turtle.Turtle()
    raphael.right(90)
    draw_semicircle(raphael, 50)

    window.exitonclick()


draw_art()
