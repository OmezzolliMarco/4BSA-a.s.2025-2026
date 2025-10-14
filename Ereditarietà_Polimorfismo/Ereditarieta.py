#definisco una classe, che diventerà classe padre di quella derivata
class Padre:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print(f"Ciao, sono {self.nome}")
    
class Figlio(Padre): #in questa riga dichiaro che la classe Figlio eredita da Padre
    def __init__(self, nome, cognome, scuola):
        super().__init__(nome, cognome) #richiamo il costruttore del padre essendo classe ereditata
        self.scuola = scuola
    def info_scuola(self):
        print(f"Sono iscritto alla scuola {self.scuola}")
    def saluta(self): #override del metodo del padre
        super().saluta()
        print(f"Vado alla scuola {self.scuola}")
    

p = Padre("Mario", "Rossi") #creo l'istanza di padre
f = Figlio("Carlo", "Rossi", "Scuola Martino Rossi") #creo l'istanza del figlio

p.saluta()
f.saluta()