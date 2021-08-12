import turtle as t

t.speed(0)
t.pensize(2)
colors = ['red', 'green', 'blue', 'black', 'cyan', 'darkgreen']

for i in range(200):
    t.color(colors[i % 5])
    t.forward(i)
    t.circle(60)
    t.penup()
    t.left(60)
    t.pendown()

t.left(200)
t.right(200)
t.done()