import tkinter as tk

def mostrar_valor(val):
    print("Valor del deslizador:", val)

root = tk.Tk()
root.title("Punto 10")
root.geometry("300x150")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=mostrar_valor)
scale.pack(pady=40)

root.mainloop()