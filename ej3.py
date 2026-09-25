import tkinter as tk

def mensaje_consola():
    print("¡El botón ha sido presionado!")

root = tk.Tk()
root.title("Punto 3")
root.geometry("300x150")

btn = tk.Button(root, text="Hacer clic", command=mensaje_consola)
btn.pack(pady=40)

root.mainloop()