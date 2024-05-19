import tkinter as tk
from cifrado_vignere import *
from preprocesamiento import solo_A_Z

class vignere_panel(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.raiz = raiz
        self.contruir_panel()

    def btn_cifrado_vignere(self):
        txt = self.txt_original.get("1.0", "end-1c")
        clave = self.txt_clave.get("1.0", "end-1c")
        txt = solo_A_Z(txt)
        clave = solo_A_Z(clave)
        txt = cifrado_vignere_27(txt, clave)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_cesar(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")
        clave = self.txt_clave.get("1.0", "end-1c")
        txt = solo_A_Z(txt)
        clave = solo_A_Z(clave)
        txt = descifrado_vignere_27(txt, clave)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)

    def contruir_panel(self):
        lbl_titulo = tk.Label(self, text="Cifrado Vignere")
        lbl_clave = tk.Label(self, text="Clave", anchor="w")
        self.txt_clave = tk.Text(self, height=1)
        lbl_original = tk.Label(self, text="Texto original", anchor='w')
        lbl_aux = tk.Label(self)
        lbl_cifrado = tk.Label(self, text="Texto cifrado", anchor='w')
        self.txt_original = tk.Text(self, height=5)
        self.txt_cifrado = tk.Text(self, height=5)
        btn_cifrar = tk.Button(self, text="Cifrar", command=self.btn_cifrado_vignere)
        btn_descifrar = tk.Button(self, text="Descifrar", command=self.btn_descifrado_cesar)

        lbl_titulo.pack()
        lbl_clave.pack(fill="x")
        self.txt_clave.pack(fill="x")
        lbl_original.pack(fill="x")
        self.txt_original.pack(fill='x')
        lbl_aux.pack()
        lbl_cifrado.pack(fill="x")
        self.txt_cifrado.pack(fill='x')
        btn_cifrar.pack()
        btn_descifrar.pack()