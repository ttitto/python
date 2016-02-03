from base import Figure

class Circle(Figure):

    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        #self._center_turtle(turtle)
        turtle.color(self.color)
        turtle.circle(self.radius)

class Pie(Circle):
    def __init__(self, radius, arg_degrees, **kwargs):
        super().__init__(radius, **kwargs)
        self.arg_degrees = arg_degrees
        
        if(any(a is None for a in [self.arg_degrees])):
            raise ValueError('Arguments missing for Pie: arg_degrees')


    def draw(self, turtle):
        turtle.color(self.color)
        turtle.goto(self.center_x, self.center_y - self.radius)
        turtle.pendown() 
        turtle.begin_fill()
        turtle.circle(self.radius, self.arg_degrees)
        turtle.goto(self.center_x, self.center_y) 
        turtle.end_fill()

class Square(Figure):

    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

class Rectangle(Figure):
    

    def __init__(self, center_x, center_y, width, height, color='black', **kwargs):
        super().__init__(center_x, center_y, color, **kwargs)
        self.width = width
        self.height = height

        if any(a is None for a in [self.width, self.height]):
            raise ValueError('Arguments for rectangle width and height missing')


    def draw(self, turtle):
        turtle.penup()
        turtle.goto(-self.height / 2, self.width / 2)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)


class Polygon(Circle):

    
    def __init__(self, radius, num_sides, **kwargs):
        super().__init__(radius, **kwargs)
        self.num_sides = num_sides

        if any(a is None for a in [self.num_sides]):
            raise ValueError('Arguments missing for Polygon: radius, num_sides')

    
    def draw(self, turtle):
        half_radius = self.radius / 2
        angle = 360 / self.num_sides
        side = 180 - angle
        turtle.color(self.color)
        turtle.penup()
        turtle.goto(self.center_x - half_radius, self.center_y - half_radius)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(side)
            turtle.left(angle)