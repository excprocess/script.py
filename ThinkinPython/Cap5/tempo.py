'''Esercizio 5.1.
Il modulo time contiene una funzione, anch’essa di nome time, che restituisce l’attuale GMT (Tempo Medio di Greenwich) riferito ad un “tempo zero”, che è un momento arbitrario
usato come punto di riferimento. Nei sistemi UNIX, questo “tempo zero” è il 1 gennaio 1970.
>>> import time
>>> time.time()
1437746094.5735958
Realizzate uno script che acquisisca il tempo attuale e lo converta in un tempo in ore, minuti e
secondi, più i giorni trascorsi dal “tempo zero"
'''

import time
giorno1= (time.time()) #1 gennaio 1970

'''
Quando vado a prendere il tempo da time.time devo dividere in giorni, ore e minuti ricordandomi che // è una divisione 
per difetto senza restro. Utilizzo % per ricavarmi il resto da convertire poi nell'unità temporale più piccola.

'''
def tempo_passato(): #dal 1970 ad oggi
    giorni = giorno1 // (60*60*24)
    resto_giorni = giorno1 % (60*60*24)
    ore = int(resto_giorni // (60*60))
    resto_ore= resto_giorni%(60*60)
    minuti= resto_giorni//60
    resto_minuti= minuti % (60*60)
    secondi= resto_ore%(60)
    print("{:,} giorni, {} ore, {} minuti e {:2.3f} secondi dal 1 gennaio 1970'.".format(giorni, ore, minuti, secondi))
    
tempo_passato()