import tkinter as tk
from tkinter import ttk

unidades = ["Byte", "KiloByte", "MegaByte", "GigaByte", "TeraByte"]
factores = {
    "Byte": 1,
    "KiloByte": 1024,
    "MegaByte": 1024**2,
    "GigaByte": 1024**3,
    "TeraByte": 1024**4
}

def convertir():
    try:
        val = float(entry_valor.get())
        origen = combo_origen.get()
        destino = combo_destino.get()

        bytes_val = val * factores[origen]
        res = bytes_val / factores[destino]

        label_resultado.config(text=f"Resultado: {res:.6g}")
    except (ValueError, KeyError):
        label_resultado.config(text="Error de entrada")

root = tk.Tk()
root.title("Conversor de Almacenamiento")
root.geometry("350x220")

tk.Label(root, text="Valor:").place(x=40, y=20)
entry_valor = tk.Entry(root, width=15)
entry_valor.place(x=150, y=20)

combo_origen = ttk.Combobox(root, values=unidades, width=12)
combo_origen.current(2)  # MB
combo_origen.place(x=30, y=60)

combo_destino = ttk.Combobox(root, values=unidades, width=12)
combo_destino.current(3)  # GB
combo_destino.place(x=180, y=60)

btn = tk.Button(root, text="Convertir", command=convertir)
btn.place(x=130, y=110)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 10, "bold"))
label_resultado.place(x=50, y=160)

root.mainloop()