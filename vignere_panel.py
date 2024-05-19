import tkinter as tk
from tkinter import ttk
from cifrado_vignere import *
from preprocesamiento import solo_A_Z, solo_ascii_191

class vignere_panel(tk.Frame):
    MODULO1 = "ABC-27"
    MODULO2 = "ASCII-191"
    modulos = [MODULO1, MODULO2]

    def __init__(self, raiz):
        super().__init__(raiz)
        self.raiz = raiz
        self.contruir_panel()

    def btn_cifrado_vignere_27(self):
        txt = self.txt_original.get("1.0", "end-1c")
        clave = self.txt_clave.get("1.0", "end-1c")
        txt = solo_A_Z(txt)
        clave = solo_A_Z(clave)
        txt = cifrado_vignere_27(txt, clave)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_vignere_27(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")
        clave = self.txt_clave.get("1.0", "end-1c")
        txt = solo_A_Z(txt)
        clave = solo_A_Z(clave)
        txt = descifrado_vignere_27(txt, clave)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)

    def btn_cifrado_vignere_191(self):
        txt = self.txt_original.get("1.0", "end-1c")
        txt = solo_ascii_191(txt)
        clave = self.txt_clave.get("1.0", "end-1c")
        clave = solo_ascii_191(clave)
        txt = cifrado_vignere_191(txt, clave)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_vignere_191(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")
        txt = solo_ascii_191(txt)
        clave = self.txt_clave.get("1.0", "end-1c")
        clave = solo_ascii_191(clave)
        txt = descifrado_vignere_191(txt, clave)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)


    def contruir_panel(self):
        lbl_titulo = tk.Label(self, text="Cifrado Vignere")
        lbl_modulo = tk.Label(self, text="Módulo")
        self.cmb_modulo = ttk.Combobox(self, values=vignere_panel.modulos)
        self.cmb_modulo.set(vignere_panel.MODULO1)
        self.cmb_modulo.bind("<<ComboboxSelected>>", self.on_cmb_select)
        lbl_clave = tk.Label(self, text="Clave", anchor="w")
        self.txt_clave = tk.Text(self, height=1)
        lbl_original = tk.Label(self, text="Texto original", anchor='w')
        lbl_aux = tk.Label(self)
        lbl_cifrado = tk.Label(self, text="Texto cifrado", anchor='w')
        self.txt_original = tk.Text(self, height=5)
        self.txt_cifrado = tk.Text(self, height=5)
        self.btn_cifrar = tk.Button(self, text="Cifrar", command=self.btn_cifrado_vignere_27)
        self.btn_descifrar = tk.Button(self, text="Descifrar", command=self.btn_descifrado_vignere_27)

        lbl_titulo.pack()
        lbl_modulo.pack(fill="x")
        self.cmb_modulo.pack()
        lbl_clave.pack(fill="x")
        self.txt_clave.pack(fill="x")
        lbl_original.pack(fill="x")
        self.txt_original.pack(fill='x')
        lbl_aux.pack()
        lbl_cifrado.pack(fill="x")
        self.txt_cifrado.pack(fill='x')
        self.btn_cifrar.pack()
        self.btn_descifrar.pack()

    def on_cmb_select(self, event):
        selected = self.cmb_modulo.get()

        if selected == vignere_panel.MODULO1:
            self.btn_cifrar.config(command=self.btn_cifrado_vignere_27)
            self.btn_descifrar.config(command=self.btn_descifrado_vignere_27)
        elif selected == vignere_panel.MODULO2:
            self.btn_cifrar.config(command=self.btn_cifrado_vignere_191)
            self.btn_descifrar.config(command=self.btn_descifrado_vignere_191)