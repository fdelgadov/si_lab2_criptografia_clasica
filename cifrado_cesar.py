A_Z = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
def cifrado_cesar(texto, desplazar):
    aux = ""
    for c in texto:
        indice = get_indice(c)
        aux += A_Z[(indice + desplazar) % 27]

    return aux

def descifrado_cesar(texto, desplazar):
    aux = ""
    for c in texto:
        indice = get_indice(c)
        aux += A_Z[(indice - desplazar) % 27]

    return aux

def get_indice(c):
    for i in range(len(A_Z)):
        if A_Z[i] == c:
            return i

    return None