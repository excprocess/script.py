def verifica_fermat(a, b, c, n):
    if n <= 2:
        print('L\'esponente deve essere maggiore di 2, altrimenti non funziona.')
    elif a**n + b**n == c**n:
        print('Santi Numi, Fermat si è sbagliato!')
    else:
        print('No, questo non è vero.')

def prompt():
    a = float(input('Inserisci il valore di a: '))
    b = float(input('Inserisci il valore di b: '))
    c = float(input('Inserisci il valore di c: '))
    n = int(input('Inserisci il valore di n: '))
    verifica_fermat(a, b, c, n)

prompt()
