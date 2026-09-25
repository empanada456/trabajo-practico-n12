import tkinter as tk
import time

def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    lbl_reloj.config(text=hora_actual)
    root.after(1000, actualizar_reloj)  # Llama a la función cada 1 segundo

root = tk.Tk()
root.title("Reloj Digital")
root.geometry("250x100")

lbl_reloj = tk.Label(root, font=("Helvetica", 32, "bold"), fg="black")
lbl_reloj.pack(expand=True)

actualizar_reloj()
root.mainloop()