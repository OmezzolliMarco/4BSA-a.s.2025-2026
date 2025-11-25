import tkinter as tk

#main
root = tk.Tk()
root.geometry("400x250")
root.title("Esercizio 2")

frm = tk.Frame(root, bg="lightblue")
frm.pack(padx=5, pady=5, fill="both", expand=True)

titolo = tk.Label(frm, text="TITOLO")
titolo.place(relx=0.5, rely=0.5, anchor="center")

box_bs = tk.Frame(frm, bg="red")
box_bs.place(x=10, y=220, height=20, width=20)

#mainloop
root.mainloop()