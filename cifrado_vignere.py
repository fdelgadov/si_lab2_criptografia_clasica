A_Z = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrado_vignere_27(texto, clave):
    aux = ""

    for i in range(len(texto)):
        it = get_indice(texto[i])
        ik = get_indice(clave[i % len(clave)])
        aux += A_Z[(it + ik) % 27]

    return aux

def descifrado_vignere_27(texto, clave):
    aux = ""
    
    for i in range(len(texto)):
        it = get_indice(texto[i])
        ik = get_indice(clave[i % len(clave)])
        aux += A_Z[(it - ik) % 27]

    return aux

def get_indice(c):
    for i in range(len(A_Z)):
        if A_Z[i] == c:
            return i