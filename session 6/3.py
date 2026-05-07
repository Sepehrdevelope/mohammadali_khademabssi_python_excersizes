import turtle

def draw_triangle(side_length):
    t = turtle.Turtle()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    turtle.done()

draw_triangle(50)
