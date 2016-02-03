import sys
import turtle

from simple import Circle, Square, Rectangle, Pie, Polygon
from loaders.loaders import JsonLoader, YamlLoader
from os import path

FIGURE_TYPES = {
    "circle": Circle,
    "square": Square,
    "rectangle": Rectangle,
    "pie": Pie,
    "polygon": Polygon
}

LOADERS = {
    ".json": JsonLoader,
    ".yaml": YamlLoader
}

def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2

def load_input_data(input_filename):
    extension = path.splitext(input_filename)[1]
    input_data = LOADERS[extension](input_filename).load()
    return input_data

def create_figures(input_data: dict):
    result = []
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            raise ValueError("Unsupported figure")
    return result

def draw_figures(figures):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('slow')
        figure.draw(t)
    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(int(main() or 0))