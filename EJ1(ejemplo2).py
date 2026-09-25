import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def mostrar_texto():
    texto = entry.get()
    label.config(text=texto)


def abrir_archivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)


def mostrar_info():
    messagebox.showinfo("Información", "Este es un mensaje informativo")


def on_right_click(event):
    messagebox.showinfo("Clic derecho", f"Clic derecho en la posición: {event.x}, {event.y}")


def on_key(event):
    label.config(text=f"Tecla presionada: {event.keysym}")


# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación Completa")
root.geometry("500x500")

# Crear widgets
label = tk.Label(root, text="Introduce texto y presiona el botón")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Mostrar texto", command=mostrar_texto)
button.pack(pady=10)

text = tk.Text(root, height=5, width=30)
text.pack(pady=10)

combobox = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)
progress["value"] = 50

menu = tk.Menu(root)
root.config(menu=menu)
submenu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=submenu)
submenu.add_command(label="Abrir", command=abrir_archivo)
submenu.add_command(label="Salir", command=root.quit)

info_button = tk.Button(root, text="Mostrar información", command=mostrar_info)
info_button.pack(pady=10)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = tk.Frame(notebook, width=400, height=280)
frame2 = tk.Frame(notebook, width=400, height=280)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

notebook.add(frame1, text='Tab 1')
notebook.add(frame2, text='Tab 2')

tree = ttk.Treeview(frame1)
tree["columns"] = ("uno", "dos")
tree.column("#0", width=100, minwidth=100)
tree.column("uno", width=100, minwidth=100)
tree.column("dos", width=100, minwidth=100)
tree.heading("#0", text="Elemento")
tree.heading("uno", text="Columna 1")
tree.heading("dos", text="Columna 2")
tree.insert("", "end", text="Elemento 1", values=("1A", "1B"))
tree.insert("", "end", text="Elemento 2", values=("2A", "2B"))
tree.pack()

root.bind("<Button-3>", on_right_click)
root.bind("<Key>", on_key)

# Iniciar el bucle de eventos
root.mainloop()