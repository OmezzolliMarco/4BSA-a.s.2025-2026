#padre
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def descrizione(self):
        return f"Veicolo {self.marca}, {self.modello}"

class Auto(Veicolo):
    def __init__(self, marca, modello, nPorte):
        super().__init__(marca, modello)
        self.nPorte = nPorte

    #override
    def descrizione(self):
        stampaBase = super().descrizione()
        print(f"{stampaBase}. Il numero di porte è {self.nPorte}")

class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo

    #override
    def descrizione(self):
        super().descrizione()
        print(f"Il tipo è {self.tipo}")

#main
a1 = Auto("Audi", "A3", 5)
m1 = Moto("Kawasaki", "Ninja", "Corsa")

a1.descrizione()
m1.descrizione()
