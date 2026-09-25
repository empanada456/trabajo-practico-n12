# Importamos tkinter y le ponemos el nombre corto "tk"
# tkinter nos permite crear ventanas y elementos gráficos.
import tkinter as tk

# Importamos dos herramientas específicas de tkinter:
# messagebox -> permite mostrar ventanas con mensajes.
# filedialog -> permite abrir el explorador de archivos.
from tkinter import messagebox, filedialog


# ============================================================
# FUNCIÓN: mostrar_texto
# ============================================================

def mostrar_texto():
    # .get() obtiene el texto que escribió el usuario
    # dentro del Entry.
    texto = entry.get()

    # Cambiamos el texto del Label por el texto que escribió
    # el usuario.
    label.config(text=texto)


# ============================================================
# FUNCIÓN: abrir_archivo
# ============================================================

def abrir_archivo():
    # Abrimos una ventana para que el usuario pueda seleccionar
    # un archivo de su computadora.
    file_path = filedialog.askopenfilename()

    # Si el usuario seleccionó un archivo, file_path tendrá
    # la ubicación del archivo.
    # Si canceló, estará vacío.
    if file_path:

        # Abrimos el archivo en modo lectura ("r").
        # encoding="utf-8" permite leer correctamente
        # caracteres como á, é, í, ó, ú y ñ.
        with open(file_path, "r", encoding="utf-8") as file:

            # Leemos todo el contenido del archivo.
            content = file.read()

            # Borramos todo lo que había anteriormente
            # en el cuadro de texto.
            # 1.0 significa: línea 1, carácter 0.
            # tk.END significa: hasta el final.
            text.delete(1.0, tk.END)

            # Insertamos el contenido del archivo
            # dentro del cuadro de texto.
            text.insert(tk.END, content)


# ============================================================
# FUNCIÓN: mostrar_info
# ============================================================

def mostrar_info():
    # Mostramos una ventana emergente con información.
    #
    # "Información" -> título de la ventana.
    # "Este es..." -> mensaje que aparecerá.
    messagebox.showinfo(
        "Información",
        "Este es un mensaje informativo"
    )


# ============================================================
# CREACIÓN DE LA VENTANA PRINCIPAL
# ============================================================

# Creamos la ventana principal de nuestra aplicación.
# Tk() crea la ventana.
root = tk.Tk()


# Definimos el título que aparecerá arriba de la ventana.
root.title("Aplicación completa")


# Definimos el tamaño de la ventana.
# 400 = ancho
# 400 = alto
root.geometry("400x400")


# ============================================================
# LABEL
# ============================================================

# Creamos un texto (Label) que aparecerá en la ventana.
#
# root -> indica que el Label pertenece a la ventana principal.
# text -> texto que queremos mostrar.
label = tk.Label(
    root,
    text="Introduce texto y presiona el botón"
)


# .pack() coloca el Label dentro de la ventana.
#
# pady=10 agrega 10 píxeles de espacio vertical
# alrededor del elemento.
label.pack(pady=10)


# ============================================================
# ENTRY
# ============================================================

# Creamos una caja de texto de una sola línea.
#
# El usuario podrá escribir aquí.
entry = tk.Entry(root)


# Colocamos el Entry en la ventana.
entry.pack(pady=10)


# ============================================================
# BOTÓN "MOSTRAR TEXTO"
# ============================================================

# Creamos un botón.
#
# text -> texto que aparece en el botón.
# command -> función que se ejecutará cuando
#            hagamos clic en el botón.
button = tk.Button(
    root,
    text="Mostrar texto",
    command=mostrar_texto
)


# Colocamos el botón en la ventana.
button.pack(pady=10)


# ============================================================
# TEXT
# ============================================================

# Creamos un cuadro de texto grande.
#
# A diferencia de Entry, Text permite escribir
# varias líneas.
#
# height=5 -> altura aproximada de 5 líneas.
# width=30 -> ancho aproximado de 30 caracteres.
text = tk.Text(
    root,
    height=5,
    width=30
)


# Colocamos el cuadro de texto en la ventana.
text.pack()


# ============================================================
# MENÚ
# ============================================================

# Creamos la barra de menú principal.
menu = tk.Menu(root)


# Le decimos a la ventana principal que utilice
# nuestro menú.
root.config(menu=menu)


# Creamos un submenú.
#
# tearoff=0 evita que el menú pueda separarse
# de la ventana como una ventana independiente.
submenu = tk.Menu(
    menu,
    tearoff=0
)


# Agregamos el submenú a la barra principal.
#
# label="Archivo" -> será el nombre que veremos
#                   en la barra de menú.
menu.add_cascade(
    label="Archivo",
    menu=submenu
)


# ============================================================
# OPCIÓN "ABRIR"
# ============================================================

# Agregamos una opción llamada "Abrir"
# dentro del menú Archivo.
#
# Cuando el usuario haga clic en "Abrir",
# se ejecutará la función abrir_archivo().
submenu.add_command(
    label="Abrir",
    command=abrir_archivo
)


# ============================================================
# OPCIÓN "SALIR"
# ============================================================

# Agregamos una opción "Salir".
#
# Cuando se haga clic, root.quit()
# cerrará la aplicación.
submenu.add_command(
    label="Salir",
    command=root.quit
)


# ============================================================
# BOTÓN "MOSTRAR INFORMACIÓN"
# ============================================================

# Creamos otro botón.
#
# Cuando se presione, ejecutará mostrar_info().
info_button = tk.Button(
    root,
    text="Mostrar información",
    command=mostrar_info
)


# Colocamos el botón en la ventana.
info_button.pack(pady=10)


# ============================================================
# BUCLE PRINCIPAL
# ============================================================

# mainloop() mantiene la ventana abierta y esperando
# las acciones del usuario.
#
# Por ejemplo:
# - hacer clic en un botón
# - escribir texto
# - abrir el menú
# - cerrar la ventana
#
# IMPORTANTE:
# Los paréntesis () son necesarios para ejecutar
# la función.
root.mainloop()
