import tkinter as tk
from tkinter import ttk

def avanzar():
    if progress["value"] < 100:
        progress["value"] += 10

root = tk.Tk()
root.title("Punto 7 - Barra de Progreso")
root.geometry("300x150")

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=20)

btn = tk.Button(root, text="Avanzar", command=avanzar)
btn.pack(pady=10)

root.mainloop()