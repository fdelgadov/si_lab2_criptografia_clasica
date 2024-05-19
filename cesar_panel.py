import tkinter as tk
from cifrado_cesar import *
from preprocesamiento import solo_A_Z

class cesar_panel(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.raiz = raiz
        self.contruir_panel()

    def btn_cifrado_cesar(self):
        txt = self.txt_original.get("1.0", "end-1c")
        txt = solo_A_Z(txt)
        desplazar = int(self.spn_desplazar.get())
        txt = cifrado_cesar(txt, desplazar)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_cesar(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")
        desplazar = int(self.spn_desplazar.get())
        txt = descifrado_cesar(txt, desplazar)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)

    def contruir_panel(self):
        lbl_titulo = tk.Label(self, text="Cifrado Cesar")
        lbl_desplazar = tk.Label(self, text="Desplazamiento")
        self.spn_desplazar = tk.Spinbox(self, from_=1, to=26)
        lbl_original = tk.Label(self, text="Texto original", anchor='w')
        lbl_aux = tk.Label(self)
        lbl_cifrado = tk.Label(self, text="Texto cifrado", anchor='w')
        self.txt_original = tk.Text(self, height=5)
        self.txt_cifrado = tk.Text(self, height=5)
        btn_cifrar = tk.Button(self, text="Cifrar", command=self.btn_cifrado_cesar)
        btn_descifrar = tk.Button(self, text="Descifrar", command=self.btn_descifrado_cesar)

        lbl_titulo.pack()
        lbl_desplazar.pack(anchor="w")
        self.spn_desplazar.pack(anchor="w")
        lbl_original.pack(fill='x')
        self.txt_original.pack(fill='x')
        lbl_aux.pack()
        lbl_cifrado.pack(fill='x')
        self.txt_cifrado.pack(fill='x')
        btn_cifrar.pack()
        btn_descifrar.pack()