#crea un programma usando tkinter che presa in input
#la misura in piedi la converte in metri (stampando
#il risultato in output)

import tkinter as tk

def converti(*args):
    try:
        valore = float(piedi.get())
        metri.set(0.3*valore)
    except:
        pass

root = tk.Tk()
root.geometry("400x200")
root.title("Piedi -> Metri")

frm = tk.Frame(root, bg="lightgreen")
frm.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#elementi interfaccia
piedi = tk.StringVar()

piedi_inserimento = tk.Entry(frm, width=7, textvariable=piedi)
piedi_inserimento.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)

piedi_inserimento.bind("<Return>", converti)

piedi_label = tk.Label(frm, text="PIEDI", bg="lightgreen")
piedi_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

#pulsante
btn = tk.Button(frm, text="=>", command=converti)
btn.grid(row=1, column=1, sticky="NSEW", pady=10)

#metri
metri = tk.StringVar()
label_conversione = tk.Label(frm, text="METRI", bg="lightgreen")
label_conversione.grid(row=0, column=2, sticky="W", padx=5, pady=5)

valore_metri = tk.Label(frm, textvariable=metri)
valore_metri.grid(row=1, column=2, sticky="W", padx=5, pady=5)

#gestione della griglia
frm.grid_columnconfigure(0, weight=2)
frm.grid_columnconfigure(1, weight=1)
frm.grid_columnconfigure(2, weight=2)

frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=2)

#mainloop
root.mainloop()
