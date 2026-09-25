# Importamos todas las herramientas de Tkinter
from tkinter import *


# ============================================================
# CREACIÓN DE LA VENTANA PRINCIPAL
# ============================================================

# Creamos la ventana principal.
# Tk() crea nuestra ventana.
raiz = Tk()


# ============================================================
# CREACIÓN DEL FRAME
# ============================================================

# Creamos un Frame.
# El Frame es como un "contenedor" donde podemos colocar
# otros elementos de nuestra interfaz.
mi_frame = Frame()


# Colocamos el Frame dentro de la ventana.
mi_frame.pack()


# ============================================================
# CONFIGURACIÓN DEL FRAME
# ============================================================

# Cambiamos el color de fondo del Frame.
mi_frame.config(bg="blue")


# Cambiamos el tamaño del Frame.
#
# width  -> ancho
# height -> alto
#
# IMPORTANTE:
# width y height van en minúscula.
mi_frame.config(width=400, height=200)


# Cambiamos el grosor del borde.
# bd significa "border width".
mi_frame.config(bd=24)


# Cambiamos el tipo de borde.
#
# "sunken" hace que el borde parezca hundido.
#
# IMPORTANTE:
# Es "relief", no "refief".
mi_frame.config(relief="sunken")


# Cambiamos el tipo de cursor cuando pasamos
# el mouse sobre el Frame.
#
# "hand2" muestra una mano.
# "arrow" muestra la flecha normal.
mi_frame.config(cursor="hand2")


# ============================================================
# BUCLE PRINCIPAL
# ============================================================

# Mantiene la ventana abierta y permite que responda
# a las acciones del usuario.
raiz.mainloop()
