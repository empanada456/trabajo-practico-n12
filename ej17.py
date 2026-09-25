import tkinter as tk
from tkinter import messagebox
import random

numero_secreto = random.randint(1, 100)

def verificar_intento():
    try:
        intento = int(entry.get())
        if intento < numero_secreto:
            messagebox.showinfo("Pista", "El número es más ALTO")
        elif intento > numero_secreto:
            messagebox.showinfo("Pista", "El número es más BAJO")
        else:
            messagebox.showinfo("¡Felicidades!", "¡Correcto! Has adivinado el número.")
    except ValueError:
        messagebox.showwarning("Atención", "Por favor ingresa un número entero.")

root = tk.Tk()
root.title("Adivina el Número")
root.geometry("300x150")

tk.Label(root, text="Adivina un número del 1 al 100:").pack(pady=10)
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

btn = tk.Button(root, text="Adivinar", command=verificar_intento)
btn.pack(pady=10)

root.mainloop()