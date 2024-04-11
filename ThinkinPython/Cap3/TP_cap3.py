# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 06:07:46 2024

@author: coraz
"""

#1
def giustif_destra(s):
    spaces= 70-len(s)
    print(spaces*('\t')+ s) 
    pass
    
giustif_destra('monty')

#2
def fai2volte(f, valore):
    f(valore)
    f(valore)
    pass

fai2volte(print, "Snugglebunnies")

def stampa2volte(bruce):
    print(bruce)
    print(bruce)
    pass

fai2volte(stampa2volte, 'spam')        

def fai_quattro(f,valore):
    fai2volte(f, valore)
    fai2volte(f, valore)
    pass

fai_quattro(print, "Snugglebunnies")
'''2. Modificate fai2volte in modo che accetti due argomenti, un oggetto funzione e un valore, e
che chiami la funzione due volte passando il valore come argomento.
3. Copiate nel vostro script la definizione di stampa_2volte che abbiamo visto nel corso di
questo capitolo.
4. Usate la versione modificata di fai2volte per chiamare stampa_2volte per due volte,
passando 'spam' come argomento.
5. Definite una nuova funzione di nome fai_quattro che richieda un oggetto funzione e un
valore e chiami la funzione per 4 volte, passando il valore come argomento. Dovrebbero esserci
solo due istruzioni nel corpo di questa funzione, non quattro.'''

#3
'''1. Scrivete una funzione che disegni una griglia come questa:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Suggerimento: per stampare più di un valore per riga, stampate una sequenza di valori
separati da virgole:
print('+', '-')
Di default, print va a capo; si può però variare questo comportamento e restare sulla stessa
riga, inserendo uno spazio, in questo modo:
print('+', end=' ')
print('-')
L’output di queste istruzioni è '+ -'.
Una funzione print priva di argomento, termina la riga e va a capo.
2. Scrivete una funzione che disegni una griglia simile, con quattro righe e quattro colonne'''

def colonne(f):
    f()
    f()
    f()
    print('\t')
    
def do_twice_riga(f):
    f()
    f()
    print('+', '\t')
    
def do_4xs(f):
    colonne(f)
    colonne(f)
    colonne(f)
    colonne(f)
    
def stampa_riga():
    print('+', end='')
    print(' -'*4, end=' ')
    pass

def stampa_colonna():
    print('|', end='')
    print(' '*8, end=' ')
    pass

do_twice_riga(stampa_riga) 
do_4xs(stampa_colonna)
do_twice_riga(stampa_riga) 
do_4xs(stampa_colonna)
do_twice_riga(stampa_riga)

#SOLUZIONE PROPOSTA
'''def do_twice(f):
    f()
    f()
    
def do_4xs(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+', end = '')
    print(' -' * 4, end = ' ')
    
def print_full_beam():
    do_twice(print_beam)
    print('+')
    
def print_struct():
    print('/', end = '')
    print(' ' * 9, end = '')
    
def print_full_struct():
    do_twice(print_struct)
    print('/')
    
def print_top_half():
    print_full_beam()
    do_4xs(print_full_struct)
    
do_twice(print_top_half)
print_full_beam()'''
