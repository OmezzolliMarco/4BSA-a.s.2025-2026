import csv #importo la libreria per la gestione dei CSV

class Persona:
    def __init__(self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta


#main
persone = []
with open("File\\CSV\\persone.csv") as documento: #documento = open("...")
    reader = csv.reader(documento, delimiter=",") #strumento per la lettura del file
    for riga in reader:
        #creare una Persona partendo dai dati letti nel CSV
        #primo metodo - ricordo che riga = ["Nome", "Cognome", ...]
        p = Persona(riga[0], riga[1], riga[2], riga[3])
        #secondo metodo
        nome, cognome, eta, citta = riga
        p = Persona(nome, cognome, eta, citta)
        #aggiungo la persona alla lista
        persone.append(p)

