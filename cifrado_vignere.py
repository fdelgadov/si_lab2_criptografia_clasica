from cifrado_cesar import get_indice, A_Z
from preprocesamiento import ascii_191

def cifrado_vignere_27(texto, clave):
    aux = ""

    for i in range(len(texto)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(clave[i % len(clave)], A_Z)
        aux += A_Z[(it + ik) % 27]

    return aux

def descifrado_vignere_27(texto, clave):
    aux = ""
    
    for i in range(len(texto)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(clave[i % len(clave)], A_Z)
        aux += A_Z[(it - ik) % 27]

    return aux

def cifrado_vignere_191(texto, clave):
    aux = ""
    
    for i in range(len(texto)):
        it = get_indice(texto[i], ascii_191)
        ik = get_indice(clave[i % len(clave)], ascii_191)
        aux += ascii_191[(it + ik) % 191]

    return aux

def descifrado_vignere_191(texto, clave):
    aux = ""
    
    for i in range(len(texto)):
        it = get_indice(texto[i], ascii_191)
        ik = get_indice(clave[i % len(clave)], ascii_191)
        aux += ascii_191[(it - ik) % 191]

    return aux