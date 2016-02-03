import turtle


def draw_chess_board(t: turtle.Turtle):
    side = 40
    for k in range(4):
        for j in range(2):
            for i in range(8):
                if i % 2 == 0:
                    t.begin_fill()
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.forward(side)
                t.left(90)
                t.end_fill()
                t.forward(side)
            side = -side
        if k != 3:
            t.right(90)
            t.forward(2 * side)
            t.left(90)
    turtle.exitonclick()


draw_chess_board(turtle.Turtle())
