import tkinter as tk

root = tk.Tk()
root.title("Punto 11 - Canvas Rectángulo")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

# Dibujar rectángulo (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 250, 150, fill="skyblue", outline="blue")

root.mainloop()