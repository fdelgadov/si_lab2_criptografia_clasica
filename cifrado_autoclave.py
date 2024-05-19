from cesar_panel import A_Z, get_indice

def cifrado_autoclave(texto, clave):
    aux = ""

    for i in range(len(clave)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(clave[i], A_Z)
        aux += A_Z[(it + ik) % 27]

    for i in range(len(clave), len(texto)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(texto[i - len(clave)], A_Z)
        aux += A_Z[(it + ik) % 27]

    return aux

def descifrado_autoclave(texto, clave):
    aux = ""

    for i in range(len(clave)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(clave[i], A_Z)
        aux += A_Z[(it - ik) % 27]

    for i in range(len(clave), len(texto)):
        it = get_indice(texto[i], A_Z)
        ik = get_indice(aux[i - len(clave)], A_Z)
        aux += A_Z[(it - ik) % 27]

    return aux