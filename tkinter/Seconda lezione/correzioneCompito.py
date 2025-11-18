import tkinter as tk

def cambiaTesto():
    label.config(text="Ciao sono Marco")

root = tk.Tk()
root.geometry("400x400")
root.title("Mostra testo")

frm = tk.Frame(root)
frm.pack(padx=5, pady=5, fill="both", expand=True)

label = tk.Label(frm, text="Nascosto")
label.pack(pady=20)

btn = tk.Button(frm, text="Cambia il testo", command=cambiaTesto)
btn.pack(pady=10)

#mainloop
root.mainloop()