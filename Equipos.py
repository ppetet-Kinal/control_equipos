import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Inventario de Sistemas")
root.geometry("900x600")

label_titulo = tk.Label(root, text="Control de Equipos", font=("Arial", 20))
label_titulo.place(x=5, y=5)

nb = ttk.Notebook(root)
nb.place(x=10, y=50, width=880, height=540)

pl = ttk.Frame(nb)
nb.add(pl, text='Control de Equipo')

p2 = tk.Frame(nb)
nb.add(p2, text='Importar')

root.mainloop()