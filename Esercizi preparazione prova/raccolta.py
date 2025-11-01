"""
ESERCIZIO 1: CONTA VOCALI E CONSONANTI
Scrivi una funzione che, dato un testo, conta quante vocali e quante consonanti contiene.
Ignora numeri, spazi e punteggiatura.
"""

def conta_vocali_consonanti(testo: str):
    vocali_set = set("aeiouAEIOU")
    consonanti = 0
    vocali = 0
    for ch in testo:
        if ch.isalpha():
            if ch in vocali_set:
                vocali += 1
            else:
                consonanti += 1
    return vocali, consonanti

# Esempio d'uso
s = "Ciao, mi chiamo Mario!"
v, c = conta_vocali_consonanti(s)
print("Vocali:", v, "Consonanti:", c)

"""
ESERCIZIO 2: PALINDROMO
Scrivi una funzione che dice se una frase è palindroma,
ignorando spazi, punteggiatura e differenze tra maiuscole e minuscole.
"""

def e_palindromo(frase: str):
    pulita = ""
    for ch in frase.lower():
        if ch.isalnum():
            pulita += ch
    return pulita == pulita[::-1] #ritorna vero se le due stringhe sono uguali

# Esempio d'uso
print(e_palindromo("I topi non avevano nipoti"))  # True
print(e_palindromo("Ciao"))                        # False

"""
ESERCIZIO 3: DIZIONARI
Dato un testo, crea un dizionario {parola: frequenza}.
Stampa la parola che appare più volte.
"""

def frequenze_parole(testo: str) -> dict:
    pulito = ""
    for ch in testo.lower():
        if ch.isalnum() or ch.isspace():
            pulito += ch
    parole = pulito.split()
    freq = {}
    for p in parole:
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return freq

# Esempio d'uso
t = "Rosa rosae rosae: rosa! La rosa è una rosa."
freq = frequenze_parole(t)
max = 0
parola_max = ""
for key, val in freq.items()
    if val > max:
        parola_max = key
        max = val

print(f"La parola che appare più volte è {parola_max} ({max} volte)")


"""
ESERCIZIO 4: DIZIONARI E LISTE
Dato un dizionario del tipo {"Anna":[8,7,9], "Luca":[6,6,7]}, 
calcola la media per ciascuno studente e stampa se è promosso (media ≥ 6).
"""

def medie_e_esito(voti: dict[str, list[int]]):
    for nome, lista_voti in voti.items():
        if len(lista_voti) == 0:
            media = 0
        else:
            s = 0
            for v in lista_voti:
                s += v
            media = s / len(lista_voti)
        esito = "Promosso"
        if media < 6:
            esito = "Non promosso"
        #uso .2f per indicare un arrotondamento alla seconda cifra
        #decimale per la media dei voti
        print(f"{nome}: media={media:.2f} -> {esito}")

# Esempio d'uso
registro = {"Anna":[8,7,9], "Luca":[6,6,7], "Marta":[5,5]}
medie_e_esito(registro)


"""
ESERCIZIO 5: CLASSI E LISTE
Definisci una classe Studente con:
- attributo nome
- lista dei voti
- metodo aggiungi_voto(v)
- metodo media()
Dati più studenti, stampa quello con la media più alta e la media generale della classe.
"""

class Studente:
    def __init__(self, nome: str):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, v: int):
        if 0 <= v <= 10:
            self.voti.append(v)

    def media(self) -> float:
        if not self.voti:
            return 0.0
        s = 0
        for v in self.voti:
            s += v
        return s / len(self.voti)

    def __str__(self):
        return f"{self.nome} (media: {self.media():.2f})"

# Creo una lista inserendo direttamente le istanze create nella lista
classe = [Studente("Anna"), Studente("Luca"), Studente("Marta")]
#si possono utilizzare gli indici su classe per accedere
#direttamente agli studenti e associare loro un voto.
#Il metodo è equivalente a creare prima una istanza e poi richiamare
#aggiungi voto
classe[0].aggiungi_voto(8) 
classe[0].aggiungi_voto(9)
classe[1].aggiungi_voto(6) 
classe[1].aggiungi_voto(7)
classe[2].aggiungi_voto(10) 
classe[2].aggiungi_voto(9)

migliore = classe[0]
somma_medie = 0
for s in classe:
    somma_medie += s.media()
    if s.media() > migliore.media():
        migliore = s
media_classe = somma_medie / len(classe)

print("Migliore:", migliore)
print(f"Media classe: {media_classe:.2f}")


"""
ESERCIZIO 6: EREDITARIETÀ
Crea una classe base Persona con attributi:
- nome
- eta

Crea due sottoclassi:
- Studente (che eredita da Persona e aggiunge "corso")
- Insegnante (che eredita da Persona e aggiunge "materia", come attributo privato, non può essere vuota)

Entrambe devono usare il costruttore del padre tramite super().__init__(...)
e ridefinire il metodo descrizione() per restituire una stringa adeguata.

Scrivi una funzione che, data una lista di persone (studenti e insegnanti),
stampi per ognuna la sua descrizione (dimostrando il polimorfismo).
"""

# Classe base
class Persona:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta

    def descrizione(self):
        return f"{self.nome}, {self.eta} anni"

# Sottoclasse Studente
class Studente(Persona):
    def __init__(self, nome: str, eta: int, corso: str):
        # Chiama il costruttore del padre per inizializzare nome ed età
        super().__init__(nome, eta)
        # Aggiunge l’attributo specifico della sottoclasse
        self.corso = corso

    def descrizione(self):
        return f"Studente: {self.nome}, {self.eta} anni, corso di {self.corso}"

# Sottoclasse Insegnante
class Insegnante(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        # Usa il costruttore del padre
        super().__init__(nome, eta)
        self.setMateria(materia)

    def setMateria(self, materia: str):
        if len(materia)>0:
            self.__materia = materia
        else:
            self.__materia = None #oppure raise ValueError(...)
        
    def getMateria(self):
        return self.__materia

    def descrizione(self):
        return f"Insegnante: {self.nome}, {self.eta} anni, insegna {self.__materia}"

def stampa_descrizioni(persone: list[Persona]):
    for p in persone:
        print(p.descrizione())

# Esempio d’uso
gruppo = [
    Studente("Anna", 17, "Informatica"),
    Studente("Luca", 18, "Matematica"),
    Insegnante("Prof. Rossi", 45, "Fisica")
]

stampa_descrizioni(gruppo)


"""
ESERCIZIO 7: LETTURA E SCRITTURA SU FILE DI TESTO
Scrivi un programma che:
1. Chiede all’utente di inserire alcune frasi e le salva in un file "frasi.txt".
2. Legge il file e conta quante parole contiene.
3. Stampa a video il numero di parole.

Suggerimento: usa i metodi open(), write(), readlines().
"""

def scrivi_file():
    with open("frasi.txt", "w") as f:
        testo = input("Inserisci un testo: ")
        if len(testo) > 0:
            f.write(testo)

def leggi_file():
    with open("frasi.txt", "r", encoding="utf-8") as f:
        contenuto = f.read()
        n_parole = contenuto.split(" ")
        print("Parole: {n_parole}")

# Esempio d’uso
scrivi_file()
leggi_file()

"""
ESERCIZIO 8: LETTURA DI UN FILE CSV (DIFFICILE)
Hai un file chiamato "voti.csv" con i seguenti dati (puoi crearlo tu con un editor di testo):

nome,materia,voto
Anna,Matematica,8
Luca,Informatica,6
Anna,Informatica,9
Luca,Matematica,7
Marta,Informatica,10

Scrivi un programma che:
1. Legge il file CSV usando il modulo csv.
2. Calcola la media dei voti per ogni studente.
3. Stampa le medie a video.
"""

import csv

def leggi_csv_e_calcola_medie(nome_file: str):
    voti_studenti = {}

    # Apertura del file in sola lettura
    with open(nome_file, "r") as file:
        reader = csv.reader(file)  # Legge ogni riga come dizionario

        for riga in reader:
            nome = riga[0]
            voto = float(riga[2])

            # Aggiunge il voto alla lista dei voti dello studente
            if nome not in voti_studenti:
                voti_studenti[nome] = []
            voti_studenti[nome].append(voto)

    # Calcolo e stampa delle medie
    print("Medie per studente:")
    for nome, voti in voti_studenti.items():
        media = sum(voti) / len(voti)
        print(f"{nome}: {media:.2f}")

# Esempio d’uso
leggi_csv_e_calcola_medie("voti.csv")
