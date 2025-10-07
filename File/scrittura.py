#creazione file con sovrascrittura
output = open("File\\output.txt", "w")

testo = "ZZZZZZZZZZZZ"
output.write(testo)

output.close()

#scrittura su file con append
output2 = open("File\\output.txt", "a")
testo = "Sono un'aggiunta..."

output2.write(testo)

output2.close()