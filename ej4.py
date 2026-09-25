import tkinter as tk

def mostrar_entrada():
    texto = entry.get()
    print("Texto ingresado:", texto)

root = tk.Tk()
root.title("Punto 4")
root.geometry("300x150")

entry = tk.Entry(root, width=25)
entry.pack(pady=15)

btn = tk.Button(root, text="Enviar a consola", command=mostrar_entrada)
btn.pack(pady=10)

root.mainloop()