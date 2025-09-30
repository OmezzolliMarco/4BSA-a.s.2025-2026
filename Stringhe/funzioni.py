#find()

stringa = "ciao"
posizione = stringa.find("ia")
print(posizione) #stampa 1 perchè indica la posizione della i dopo aver trovato ia
#se non trova la sottostringa ritorna -1

#funzione split con limite
nome = "Vincenzo Rania Maria"
parti = nome.split(" ", 1)
print(parti)


#strip
spazi = "   Ciao"
print(spazi.strip())

#rimozione degli spazi con replace
originale = " Ciao a tutti   "
originale = originale.strip()
originale = originale.replace(" ", "")


#rimozione degli spazi con ciclo
sanificata = ""
for c in originale:
    if c != " ":
        sanificata += c

print(sanificata) 