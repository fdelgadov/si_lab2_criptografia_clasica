import sys
from cifrado_cesar import *
from preprocesamiento import solo_A_Z
from cifrado_vignere import ascii_191

def t1_cifrado_cesar():
    texto = "Hola mundo"
    desplazar = 3
    texto = solo_A_Z(texto)
    cifrado = cifrado_cesar(texto, desplazar)
    descifrado = descifrado_cesar(cifrado, desplazar)
    print(f"Cifrado\n{cifrado}\n\nDescrifrado\n{descifrado}")

def t2_revision_ascii_191():
    aux = ""

    for i in range(len(ascii_191)):
        aux += f"[{i}] {ascii_191[i]}\n"
    print(aux)

_ = sys.argv
if _[1] == '1':
    t1_cifrado_cesar()
elif _[1] == '2':
    t2_revision_ascii_191()