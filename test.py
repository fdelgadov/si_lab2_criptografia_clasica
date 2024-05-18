import sys
from cifrado_cesar import *
from preprocesamiento import solo_A_Z

def t1_cifrado_cesar():
    texto = "Hola mundo"
    desplazar = 3
    texto = solo_A_Z(texto)
    cifrado = cifrado_cesar(texto, desplazar)
    descifrado = descifrado_cesar(cifrado, desplazar)
    print(f"Cifrado\n{cifrado}\n\nDescrifrado\n{descifrado}")

_ = sys.argv
if _[1] == '1':
    t1_cifrado_cesar()