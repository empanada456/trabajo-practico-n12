import tkinter as tk

def anadir_tarea():
    tarea = entry.get()
    if tarea:
        listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)

def eliminar_tarea():
    try:
        seleccion = listbox.curselection()
        listbox.delete(seleccion[0])
    except IndexError:
        pass

root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("300x350")

entry = tk.Entry(root, width=22)
entry.place(x=20, y=20)

btn_add = tk.Button(root, text="Añadir", command=anadir_tarea)
btn_add.place(x=200, y=15)

listbox = tk.Listbox(root, width=35, height=12)
listbox.place(x=20, y=60)

btn_del = tk.Button(root, text="Eliminar", command=eliminar_tarea)
btn_del.place(x=110, y=280)

root.mainloop()