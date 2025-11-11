import tkinter as tk

#funzioni
def conteggio():
    global conta
    conta += 1
    label.config(text=f"Numero click: {conta}") #aggiorno l'elemento

root = tk.Tk()
root.title("Piedi -> Metri")
root.geometry("400x200")

#creazione del frame contenitore
frm = tk.Frame(root, bg="red")
frm.pack(padx=5, pady=5, fill="both", expand=True)

conta = 0

#label
label = tk.Label(frm, text=f"Numero click: {conta}", font=("Arial", 16), bg="lightblue")
label.pack(pady=40)

#creazione bottone da cliccare
button = tk.Button(frm, text="Cliccami!", command=conteggio, )
button.pack(pady=15)

#mainloop
root.mainloop()
