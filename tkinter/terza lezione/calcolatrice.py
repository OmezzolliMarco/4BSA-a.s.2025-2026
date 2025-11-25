import tkinter as tk

#funzioni
def operazione(testo):
    schermo.config(text=testo)

#main
root = tk.Tk()
root.geometry("400x600")
root.title("CalcolaMax")

frm = tk.Frame(root, bg="white")
frm.pack(fill="both", expand="true")

frm_superiore = tk.Frame(frm, bg="red")
frm_superiore.pack()

frm_inferiore = tk.Frame(frm, bg="green")
frm_inferiore.pack()

#gestione frame superiore
uguale = tk.Button(frm_superiore, text="=")
uguale.grid(column=0, row=0, sticky="W")

schermo = tk.Label(frm_superiore, text="")
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