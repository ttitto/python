import turtle


def draw_square_with_turtle(drawer: turtle.Turtle):
    drawer.color('red')
    drawer.speed('slowest')
    step = int(input())
    drawer.forward(step)
    drawer.left(90)
    drawer.forward(step)
    drawer.left(90)
    drawer.forward(step)
    drawer.left(90)
    drawer.forward(step)


draw_square_with_turtle(turtle.Turtle())
