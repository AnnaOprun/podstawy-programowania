import turtle

def draw_square(length, pen=None):
    
    if pen is None:     # Jeśli nie przekazano gotowego pisaka, tworzymy nowego żółwia
        pen = turtle.Turtle()
        pen.speed(5)
    
    for _ in range(4):  # Kwadrat ma 4 równe boki i kąty 90 stopni
        pen.forward(length)
        pen.right(90)

def draw_trangle(length, pen=None):
    
    if pen is None:     # Rysuje trójkąt równoboczny o zadanym boku length (kąty zewnętrzne 120 stopni)
        pen = turtle.Turtle()
        pen.speed(5)

    for _ in range(3):
        pen.forward(length)
        pen.left(120)


def draw_rectangle(lenght_a, lenght_b, pen=None):   # Rysuje prostokąt o bokach lenght_a oraz lenght_b
    
    if pen is None:
        pen = turtle.Turtle()
        pen.speed(5)

    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)