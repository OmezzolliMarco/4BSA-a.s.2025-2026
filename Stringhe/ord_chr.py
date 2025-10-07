parola = input("Inserisci una parola: ")
parola = parola.strip().lower() #rimozione eventuali spazi inizio e fine

modificata = ""

for c in parola:
    ascii = ord(c)
    if ascii == 122: #se sei z
        ascii = 97
    else:
        ascii += 1

    modificata += chr(ascii)

print(modificata)
    
