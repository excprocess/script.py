# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:23:35 2024

@author: coraz
"""
#turtle_for
import turtle
bob = turtle.Turtle()
'''for i in range(4):
   bob.fd(100)
   bob.lt(90)
print(bob)
turtle.mainloop()

#exerc
1. Scrivete una funzione di nome quadrato che richieda un parametro di nome t, che è
una tartaruga. La funzione deve usare la tartaruga per disegnare un quadrato.
Scrivete una chiamata alla funzione quadrato che passi bob come argomento, ed
eseguite nuovamente il programma.'''
#mia soluzione
import turtle
def quadrato(t):
   t = turtle.Turtle()
   for i in range(4):
      t.fd(100)
      t.lt(90)
   print(t)
   turtle.mainloop()
#quadrato('bob')

'''def quadrato(t):
   for i in range(4):
      t.fd(100)
      t.lt(90)
   quadrato(bob)'''




'''
2. Aggiungete a quadrato un nuovo parametro di nome lunghezza. Modificate il corpo
in modo che la lunghezza dei lati sia pari a lunghezza, quindi modificate la chiamata alla funzione in modo da fornire un secondo argomento. Eseguite di nuovo il
programma e provatelo con vari valori di lunghezza.
bob = 'bob

def quadrato(t, lunghezza):
   t = turtle.Turtle()
   for i in range(4):
      t.fd(lunghezza)
      t.lt(90)
#quadrato(bob, 1000)'''
   
'''
3. Fate una copia di quadrato e cambiate il nome in poligono. Aggiungete un altro
parametro di nome n e modificate il corpo in modo che sia disegnato un poligono
regolare di n lati. Suggerimento: gli angoli esterni di un poligono regolare di n lati
misurano 360/n gradi.'''

def poligono(t,n):
   t = turtle.Turtle()
   for i in range(n):
      t.fd(1)
      t.lt(360/n)
   print(t)
   turtle.mainloop()
poligono('bob', 90)

'''
4. Scrivete una funzione di nome cerchio che prenda come parametri una tartaruga,
t, e un raggio, r, e che disegni un cerchio approssimato chiamando poligono con
un’appropriata lunghezza e numero di lati. Provate la funzione con diversi valori di
r.
Suggerimento: pensate alla circonferenza del cerchio e accertatevi che lunghezza *
n = circonferenza.

def cerchio(t, r):
   t = turtle.Turtle()
   for i in range(r):
      t.fd(1)
      t.lt(360/r)
   print(t)
   turtle.mainloop()
#cerchio(bob, 200)'''

'''
5. Create una versione più generale della funzione cerchio, di nome arco, che richieda
un parametro aggiuntivo angolo, il quale determina la porzione di cerchio da disegnare. angolo è espresso in gradi, quindi se angolo=360, arco deve disegnare un
cerchio completo'''

#errato!!!
def cerchio_con_angolo(t, r, arco):
   t = turtle.Turtle()
   for i in range(r):
      t.fd(1)
      t.lt(arco/r)
   print(t)
   turtle.mainloop()
#cerchio_con_angolo(bob, 200, 30)

import math

#angolo

def polilinea(t, n, lunghezza, angolo):
   for i in range(n):
      t.fd(lunghezza)
      t.lt(angolo)

'''def poligono(t, n, lunghezza):
   angolo = 360.0 / n
   polilinea(t, n, lunghezza, angolo)'''

def arco(t, r, angolo):
   arco_lunghezza = 2 * math.pi * r * angolo / 360
   n = int(arco_lunghezza / 3) + 1
   passo_lunghezza = arco_lunghezza / n
   passo_angolo = float(angolo) / n
   polilinea(t, n, passo_lunghezza, passo_angolo)

def cerchio(t, r):
   arco(t, r, 360)

#arco(bob, 100, 50)

