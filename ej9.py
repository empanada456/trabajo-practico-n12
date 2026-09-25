import tkinter as tk

def mostrar_estado():
    print(f"Estado Check 1: {var1.get()} | Estado Check 2: {var2.get()}")

root = tk.Tk()
root.title("Punto 9")
root.geometry("300x150")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

c1 = tk.Checkbutton(root, text="Casilla 1", variable=var1, command=mostrar_estado)
c2 = tk.Checkbutton(root, text="Casilla 2", variable=var2, command=mostrar_estado)

c1.pack(pady=10)
c2.pack(pady=10)

root.mainloop()