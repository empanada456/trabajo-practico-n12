import tkinter as tk
from tkinter import ttk

def elemento_seleccionado(event):
    print("Elemento seleccionado:", combo.get())

root = tk.Tk()
root.title("Punto 6")
root.geometry("300x150")

combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3", "Opción 4"])
combo.pack(pady=40)
combo.bind("<<ComboboxSelected>>", elemento_seleccionado)

root.mainloop()