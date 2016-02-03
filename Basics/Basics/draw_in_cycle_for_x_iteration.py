import turtle


def draw_in_cycle_for_x_iteration():
    g = 134
    l = 120
    iterations_count = input('Please, insert number of iterations: ')
    for i in range(int(iterations_count)):
        turtle.left(g)
        turtle.forward(l)

draw_in_cycle_for_x_iteration()
