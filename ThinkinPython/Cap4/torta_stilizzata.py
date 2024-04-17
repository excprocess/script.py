import turtle
bob = turtle.Turtle()

def isosceles(t, leg, base_angle, base):
    """
    Questa funzione disegna un triangolo isoscele a patto che i parametri inseriti
    siano corretti. Va accompagnata ad una funzione plogono che ne disegni uno con l'accortezza di calcolare
    correttamente la base e gli angoli.
    """

    t.fd(leg)
    t.lt(180 + base_angle)
    t.fd(base)
    t.lt(180 + base_angle)
    t.fd(leg)



