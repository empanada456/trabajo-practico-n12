import tkinter as tk 
from tkinter import filedialog, messagebox 

def abrir_archivo(): 
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")]) 
    if file_path: 
        with open(file_path, "r", encoding="utf-8") as f: 
            text_area.delete(1.0, tk.END) 
            text_area.insert(tk.END, f.read()) 

def guardar_archivo(): 
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")]) 
    if file_path: 
        with open(file_path, "w", encoding="utf-8") as f: 
            # El '-1c' evita que se agregue un salto de línea extra cada vez que guardás
            f.write(text_area.get(1.0, tk.END + "-1c")) 

def cambiar_tamano(): 
    # Validamos que sea un número válido antes de cambiar la fuente
    try:
        val = int(spin.get())
        text_area.config(font=("Arial", val)) 
    except ValueError:
        pass

root = tk.Tk() 
root.title("Editor de Texto") 
root.geometry("500x400") 

# Menú 
menu_bar = tk.Menu(root) 
root.config(menu=menu_bar) 

menu_archivo = tk.Menu(menu_bar, tearoff=0) 
menu_archivo.add_command(label="Abrir", command=abrir_archivo) 
menu_archivo.add_command(label="Guardar", command=guardar_archivo) 
menu_archivo.add_separator() 
menu_archivo.add_command(label="Salir", command=root.quit) 
menu_bar.add_cascade(label="Archivo", menu=menu_archivo) 

# Selector de tamaño de letra 
frame_top = tk.Frame(root) 
frame_top.pack(fill=tk.X, padx=5, pady=5) 

tk.Label(frame_top, text="Tamaño de letra:").pack(side=tk.LEFT) 

# Usamos 'command=cambiar_tamano' directamente sin lambda para leer del widget actualizado
spin = tk.Spinbox(frame_top, from_=8, to=40, width=5, command=cambiar_tamano) 
# Corrección del error .setValue() -> Se borra lo que haya y se inserta el valor por defecto
spin.delete(0, "end")
spin.insert(0, "12")
spin.pack(side=tk.LEFT, padx=5) 

text_area = tk.Text(root, font=("Arial", 12)) 
text_area.pack(fill=tk.BOTH, expand=True) 

root.mainloop()