import tkinter as tk
import random

def jugar(eleccion_usuario):
    opciones = ["Piedra", "Papel", "Tijeras"]
    eleccion_cpu = random.choice(opciones)
    emojis = {"Piedra": "🪨", "Papel": "📄", "Tijeras": "✂️"}
    
    lbl_cpu.config(text=f"Computadora: {eleccion_cpu} {emojis[eleccion_cpu]}")

    if eleccion_usuario == eleccion_cpu:
        res = "¡Empate!"
        color = "#555555" # Gris
    elif (eleccion_usuario == "Piedra" and eleccion_cpu == "Tijeras") or \
         (eleccion_usuario == "Papel" and eleccion_cpu == "Piedra") or \
         (eleccion_usuario == "Tijeras" and eleccion_cpu == "Papel"):
        res = "¡Ganaste!"
        color = "#2e7d32" # Verde
    else:
        res = "Perdiste"
        color = "#c62828" # Rojo

    lbl_resultado.config(text=res, fg=color)

root = tk.Tk()
root.title("Piedra, Papel o Tijeras")
root.geometry("320x220")

tk.Label(root, text="Elige tu opción:", font=("Arial", 12)).pack(pady=10)

frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

# Agregamos los emojis también a los botones
tk.Button(frame_btn, text="🪨 Piedra", font=("Arial", 10), command=lambda: jugar("Piedra")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_btn, text="📄 Papel", font=("Arial", 10), command=lambda: jugar("Papel")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_btn, text="✂️ Tijeras", font=("Arial", 10), command=lambda: jugar("Tijeras")).pack(side=tk.LEFT, padx=5)

lbl_cpu = tk.Label(root, text="Computadora: -", font=("Arial", 11))
lbl_cpu.pack(pady=15)

lbl_resultado = tk.Label(root, text="¿Quién ganará?", font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=5)

root.mainloop()