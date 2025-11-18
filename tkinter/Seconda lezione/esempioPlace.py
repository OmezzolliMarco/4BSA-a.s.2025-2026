#posiziona un quadrato 20x20 in varie zone della root

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Posizionamento place")

frm = tk.Frame(root, bg="red")
frm.place(width=20, height=20, relx=0.45, rely=0.45)

#mainloop
root.mainloop()