import tkinter as tk

def mostrar_opcion():
    print("Opción seleccionada:", var.get())

root = tk.Tk()
root.title("Punto 8")
root.geometry("300x200")

var = tk.StringVar(value="Ninguna")

r1 = tk.Radiobutton(root, text="Opción A", variable=var, value="Opción A", command=mostrar_opcion)
r2 = tk.Radiobutton(root, text="Opción B", variable=var, value="Opción B", command=mostrar_opcion)
r3 = tk.Radiobutton(root, text="Opción C", variable=var, value="Opción C", command=mostrar_opcion)

r1.pack(pady=5)
r2.pack(pady=5)
r3.pack(pady=5)

root.mainloop()