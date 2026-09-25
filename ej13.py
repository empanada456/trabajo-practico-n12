import tkinter as tk

def click_boton(valor):
    if valor == "=":
        try:
            resultado = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(resultado))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif valor == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, valor)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, font=("Arial", 16), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

r = 1
c = 0
for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, font=("Arial", 14), width=5, height=2,
                    command=lambda b=btn_text: click_boton(b))
    btn.grid(row=r, column=c, padx=2, pady=2)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()