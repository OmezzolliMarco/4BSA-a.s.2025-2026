import tkinter as tk

#sezione variabili globali
numero1 = 0
numero2 = 0
operazione = ""

#funzioni
def operazione(testo: str):
    if testo.isdigit():
        #è una cifra numerica
        vecchio_valore = valore.get() #prendo quanto scritto attualmente nella label
        vecchio_valore += testo #aggiungo alla stringa il testo indicato
        valore.set(vecchio_valore) #imposto la stringvar e automaticamente aggiorno la label
    elif testo == ">":
        vecchio_testo = valore.get()
        vecchio_testo = vecchio_testo[:-1]
        valore.set(vecchio_testo)
    elif testo == ",":
        pass
    else:
        #gestire l'operazione
        global numero1
        global operazione
        operazione = testo
        numero1 = valore.get()
        valore.set("")

def calcolaRisultato():
    global numero2
    numero2 = valore.get()
    #operazioni
    if operazione == "+":
        #somma + conversione
        n1 = float(numero1)
        n2 = float(numero2)
        somma = n1+n2
        valore.set(str(somma))


#main
root = tk.Tk()
root.geometry("400x600")
root.title("CalcolaMax")

frm = tk.Frame(root, bg="white")
frm.pack(fill="both", expand="true")

frm_superiore = tk.Frame(frm, bg="red")
frm_superiore.pack(fill="x")

frm_inferiore = tk.Frame(frm, bg="green")
frm_inferiore.pack()

#gestione frame superiore
uguale = tk.Button(frm_superiore, text="=", command=calcolaRisultato)
uguale.grid(column=0, row=0, sticky="W")

valore = tk.StringVar() #variabile globale
schermo = tk.Label(frm_superiore, textvariable=valore)
schermo.grid(column=1, row=0, sticky="W")

frm_superiore.grid_rowconfigure(0, weight=1)
frm_superiore.grid_columnconfigure(0, weight=1)
frm_superiore.grid_columnconfigure(1, weight=3)


#gestione del frame inferiore
pulsanti = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("+", 0, 3),
    ("6", 1, 0),
    ("5", 1, 1),
    ("4", 1, 2),
    ("-", 1, 3),
    ("3", 2, 0),
    ("2", 2, 1),
    ("1", 2, 2),
    ("x", 2, 3),
    (">", 3, 0),
    ("0", 3, 1),
    (",", 3, 2),
    ("/", 3, 3)
]

for (testo, riga, colonna) in pulsanti:
    #funzioni anonime
    btn = tk.Button(frm_inferiore, text=testo, command=lambda t=testo: operazione(t))
    btn.grid(row=riga, column=colonna, sticky="NSEW", padx=5, pady=5)

#mainloop
root.mainloop()