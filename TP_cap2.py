'''1. Il volume di una sfera di raggio r 4/3 pir^3. Che volume ha una sfera di raggio 5?

2. Il prezzo di copertina di un libro Ã¨ Â¿ 24,95, ma una libreria ottiene il 40% di sconto. I costi
di spedizione sono Â¿ 3 per la prima copia e 75 centesimi per ogni copia aggiuntiva. Qual Ã¨ il
costo totale di 60 copie?
'''

#1
r= 2 #inserisci il numero (float(input('numero raggio:')))
pi=3.14
Volume= 4*(pi*r**3)/3
print('#1\n' + str(Volume))

#2
libro= 24.95
percentuale= float(40)
sconto= float(100-percentuale)
libro_scontato= (float(libro)/100*(sconto))
copie= 60
spedizione1= 3
spedizioni_successiive= 0.75
totale= libro_scontato + spedizione1 + ((libro_scontato + 0.75)*(copie-1))
print('#2\n' + str(totale))