#crea un'istanza di un documento (riferita ad un file specifico)
documento = open("File\\prova.txt")
#richiamo un metodo su documento per la lettura del contenuto
contenuto = documento.read() #contenuto = stringa

#stampo il contenuto
print(contenuto)

#quando il documento non mi serve più
documento.close()