import tkinter as tk

root = tk.Tk()
root.title("Punto 12 - Figuras e Imagen")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Rectángulo
canvas.create_rectangle(20, 20, 120, 80, fill="lightgreen", outline="green")

# Círculo (oval con lados iguales)
canvas.create_oval(150, 20, 230, 100, fill="coral", outline="red")

# Triángulo (tres pares de coordenadas: x1,y1, x2,y2, x3,y3)
canvas.create_polygon(300, 100, 250, 20, 350, 20, fill="yellow", outline="orange")

# Imagen
try:
    img = tk.PhotoImage(file="animal.png")
    canvas.create_image(200, 250, image=img)
except Exception:
    canvas.create_text(200, 250, text="[Coloque animal.png en el directorio]")

root.mainloop()