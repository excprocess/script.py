import turtle
bob = turtle.Turtle()

def torta(t, length, n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

torta(bob, 30, 10)

turtle.mainloop()


