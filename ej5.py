import tkinter as tk
from tkinter import colorchooser

def cambiar_color():
    color = colorchooser.askcolor(title="Seleccionar color")
    # color es una tupla: ((R, G, B), "#HEX")
    if color[1]:
        root.config(bg=color[1])
        print("Código hexadecimal del color:", color[1])

root = tk.Tk()
root.title("Punto 5 - Selector de Color")
root.geometry("300x200")

btn = tk.Button(root, text="Seleccionar Color", command=cambiar_color)
btn.pack(pady=70)

root.mainloop()