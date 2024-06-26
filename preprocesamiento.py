import math
from functools import reduce

caracter_sustituto = {
    'a': 'u',
    'h': 't',
    'ñ': 'e',
    'k': 'l',
    'v': 'f',
    'w': 'b',
    'z': 'y',
    'r': 'p'
}

tildes_vocales = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U'
}

signos = [' ', ',', '.', ';', '\n']

ascii_191 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~‘’¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
A_Z = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def sustituciones(txt):
    aux = txt
    for k, v in caracter_sustituto.items():
        aux = aux.replace(k, v)
        if k != 'ñ':
            aux = aux.replace(chr(ord(k) - 32), chr(ord(v) - 32))
        else:
            aux = aux.replace('Ñ', 'E')

    return aux

def eliminar_tildes(txt):
    aux = txt
    for k, v in tildes_vocales.items():
        aux = aux.replace(k, v)
    return aux

def a_mayuscula(txt):
    aux = txt

    for x in range(97, 123):
        aux = aux.replace(chr(x), chr(x - 32))

    aux = aux.replace('ñ', 'Ñ')

    return aux

def eliminar_signos(txt):
    validos = A_Z
    aux = ""

    for c in txt:
        if c in validos:
            aux += c

    return aux

def preprocesamiento(texto):
    res = texto
    res = sustituciones(res)
    res = eliminar_tildes(res)
    res = a_mayuscula(res)
    res = eliminar_signos(res)

    return res

def frecuencias(archivo):
    with open(archivo, 'r', encoding="utf-8") as archivo:
        txt = archivo.read()

    diccionaro_frecuencias = {chr(x): 0 for x in range(65, 91)}
    diccionaro_frecuencias['Ñ'] = 0

    for c in txt:
        diccionaro_frecuencias[c] += 1

    return diccionaro_frecuencias

def secuencias_repetidas(texto, tamaño):
    secuencias = {}
    for i in range(len(texto) - tamaño):
        secuencia = texto[i:i + tamaño]
        try:
            secuencias[secuencia].append(i)
        except:
            secuencias[secuencia] = [i]

    return {k: v for k, v in secuencias.items() if len(v) > 1}
    
def calcular_distancias(secuencias):
    distancias = []
    for posiciones in secuencias.values():
        for i in range(len(posiciones) - 1):
            distancias.append(posiciones[i + 1] - posiciones[i])
    return distancias

def mcd_lista(numbers):
    return reduce(math.gcd, numbers)

def caracter_frecuente(texto):
    frecuente = -1
    frecuencia = -1
    for c in A_Z:
        aux = 0
        for cc in texto:
            if c == cc:
                aux += 1
        if frecuencia < aux:
            frecuencia = aux
            frecuente = c

    return [frecuente, frecuencia]
        
def a_unicode(texto):
    aux = ""
    for c in texto:
        hexa = f"{hex(ord(c))}"
        aux += f"{hexa[2:]}"

    return aux

def otra_sustitucion(txt):
    aux = ""
    for c in txt:
        aux += chr(ord(c) + 100)

    return aux

def insertar_epis(txt):
    aux = txt[0]

    for i in range(1, len(txt)):
        if i % 13 == 0:
            aux += "EPIS"
        aux += txt[i]

    mod = len(aux) % 5
    if mod != 0:
        aux += "ZZZZ"[:(5 - mod)]

    return aux
    
def solo_A_Z(texto):
    aux = texto
    aux = eliminar_tildes(aux)
    aux = a_mayuscula(aux)
    aux = eliminar_signos(aux)

    return aux

def solo_ascii_191(texto):
    aux = ""

    for c in texto:
        if c in ascii_191:
            aux += c

    return aux