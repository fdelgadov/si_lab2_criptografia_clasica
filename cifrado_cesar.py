A_Z = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
def cifrado_cesar(texto, desplazar):
    aux = ""
    for c in texto:
        indice = get_indice(c, A_Z)
        aux += A_Z[(indice + desplazar) % 27]

    return aux

def descifrado_cesar(texto, desplazar):
    aux = ""
    for c in texto:
        indice = get_indice(c, A_Z)
        aux += A_Z[(indice - desplazar) % 27]

    return aux

def get_indice(c, l):
    for i in range(len(l)):
        if l[i] == c:
            return i
    return None