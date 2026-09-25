import tkinter as tk
from tkinter import ttk

def convertir():
    try:
        val = float(entry_valor.get())
        origen = combo_origen.get()
        destino = combo_destino.get()

        if origen == destino:
            res = val
        elif origen == "Metros" and destino == "Kilómetros":
            res = val / 1000
        elif origen == "Kilómetros" and destino == "Metros":
            res = val * 1000
        
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido")

root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("350x220")

tk.Label(root, text="Valor:").place(x=40, y=20)
entry_valor = tk.Entry(root, width=15)
entry_valor.place(x=150, y=20)

combo_origen = ttk.Combobox(root, values=["Metros", "Kilómetros"], width=12)
combo_origen.current(0)
combo_origen.place(x=30, y=60)

combo_destino = ttk.Combobox(root, values=["Metros", "Kilómetros"], width=12)
combo_destino.current(1)
combo_destino.place(x=180, y=60)

btn = tk.Button(root, text="Convertir", command=convertir)
btn.place(x=130, y=110)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 10, "bold"))
label_resultado.place(x=100, y=160)

root.mainloop()