import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")

a = 0
b = 0

t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()

while b < 210:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1

t.hideturtle()  # Colocando aqui para esconder a tartaruga após o desenho

turtle.done()  # Este comando deve ser chamado uma vez, após o fim do desenho
