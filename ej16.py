import tkinter as tk

def anadir_contacto():
    nombre = entry_nombre.get()
    tel = entry_tel.get()
    if nombre and tel:
        listbox.insert(tk.END, f"{nombre} - {tel}")
        entry_nombre.delete(0, tk.END)
        entry_tel.delete(0, tk.END)

def eliminar_contacto():
    try:
        seleccion = listbox.curselection()
        listbox.delete(seleccion[0])
    except IndexError:
        pass

root = tk.Tk()
root.title("Agenda de Contactos")
root.geometry("280x380")

tk.Label(root, text="Nombre:").place(x=20, y=20)
entry_nombre = tk.Entry(root, width=20)
entry_nombre.place(x=90, y=20)

tk.Label(root, text="Teléfono:").place(x=20, y=50)
entry_tel = tk.Entry(root, width=20)
entry_tel.place(x=90, y=50)

btn_add = tk.Button(root, text="Añadir", command=anadir_contacto)
btn_add.place(x=100, y=90)

listbox = tk.Listbox(root, width=30, height=10)
listbox.place(x=30, y=130)

btn_del = tk.Button(root, text="Eliminar", command=eliminar_contacto)
btn_del.place(x=100, y=320)

root.mainloop()