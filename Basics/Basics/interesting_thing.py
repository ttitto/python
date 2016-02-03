import turtle


def interesting_thing():
    i = 10
    while True:
        if i % 3 == 0:
            turtle.left(i % 96)
            turtle.backward(40)
            i += 1
        else:
            turtle.left(i % 48)
            turtle.forward(10)
            i += 1

interesting_thing()
