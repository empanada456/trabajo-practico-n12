import tkinter as tk

root = tk.Tk()
root.title("Punto 2")
root.geometry("300x150")

label = tk.Label(root, text="Hola, Mundo!", font=("Arial", 14))
label.pack(pady=40)

root.mainloop()