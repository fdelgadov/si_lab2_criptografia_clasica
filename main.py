import tkinter as tk
from cesar_panel import cesar_panel

def mostrar_cesar():
    panel1.pack()

def mostrar_panel2():
    panel1.pack_forget()

raiz = tk.Tk()
raiz.title("Algoritmos de cifrado")
raiz.geometry("640x360")

btn_cesar = tk.Button(raiz, text="Cesar", command=mostrar_cesar)

btn_cesar.pack()

panel1 = cesar_panel(raiz)

mostrar_cesar()

raiz.mainloop()