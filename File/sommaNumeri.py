file = open("File\\numeri.txt")

contenuto = file.read()

file.close()

#inizio la logica per la somma dei numeri
numeri = contenuto.split() #una lista di numeri in formato stringa

somma = 0
for numero in numeri:
    valore = int(numero)
    somma += valore

print(somma)