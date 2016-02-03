import turtle


def draw_in_cycle(drawer:turtle.Turtle, angle, side):
    drawer.color('green')
    while True:
        drawer.left(angle)
        drawer.forward(side)


side = int(input('Insert side size: '))
angle = int(input('Insert rotation angle: '))
draw_in_cycle(turtle.Turtle(), angle, side)
