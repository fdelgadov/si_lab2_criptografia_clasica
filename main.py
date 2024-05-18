import tkinter as tk
from tkinter import ttk
from cesar_panel import cesar_panel

def mostrar_panel(panel):
    global panel_actual
    panel_actual.pack_forget()
    panel_actual = panel
    panel_actual.pack()

def on_cmb_select(event):
    selected = cmb_funcionalidad.get()

    if selected == "Cesar":
        mostrar_panel(panel1)
    elif selected == "Vignere":
        mostrar_panel(panel2)

raiz = tk.Tk()
raiz.title("Algoritmos de cifrado")
raiz.geometry("640x360")

funciones = ["Cesar", "Vignere"]
cmb_funcionalidad = ttk.Combobox(raiz, values=funciones)
cmb_funcionalidad.set("Cesar")
cmb_funcionalidad.bind("<<ComboboxSelected>>", on_cmb_select)
cmb_funcionalidad.pack()

panel1 = cesar_panel(raiz)
panel2 = cesar_panel(raiz)

panel_actual = panel1
panel1.pack()

raiz.mainloop()