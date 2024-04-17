'''1. Scrivete una funzione di nome verifica_fermat che richieda quattro parametri—a, b, c e
n—e controlli se il teorema regge. Se n è maggiore di 2 e fosse
an + bn = cn
il programma dovrebbe visualizzare: “Santi Numi, Fermat si è sbagliato!”, altrimenti: “No,
questo non è vero.'''

def verifica_fermat(a,b,c,n):
    #con if verifico le condizioni imposte dal problema e stampo i relativi prompt
    if n<=2:
        print('esponente <2, non funziona')
    elif a**n + b**n == c**n:
        print('Santi Numi, Fermat si è sbagliato!')
    else: 
        print('No, questo non è vero.')
        
def prompt():
    #prendo gli input da tastiera richiesti
    a=int(input('valore di a'))
    b=int(input('valore di b'))
    c=int(input('valore di c'))
    n=int(input('valore di n'))
    verifica_fermat(a,b,c,n)
    
prompt()