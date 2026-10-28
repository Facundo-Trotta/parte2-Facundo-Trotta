import funciones
# no aceptar los numeros negativos
def no_negativo(numero):
    """
    Verifica si una cadena contiene un número entero no negativo.

    Args:
        numero (str): Cadena de caracteres que se desea validar.

    Returns:
        bool: True si contiene solamente dígitos y no está vacía;
        False en caso contrario.
    """
    es_valido = len(numero) > 0
    for caracter in numero:
        if caracter < "0" or caracter > "9":
            es_valido = False
    return es_valido

# 
def entero_no_negativo(mensaje):
    """
    Solicita un número entero no negativo y valida su ingreso.

    Args:
        mensaje (str): Mensaje que se muestra al solicitar el número.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    numero = input(mensaje)
    while not no_negativo(numero):
        print("Error: debe ingresar un número entero igual o mayor a 0.")
        numero = input(mensaje)
    return int(numero)

# pedir una opcion
def ingresar_opcion ():
    """
    Solicita una opción del menú y valida que esté entre 0 y 11.

    Returns:
        int: Opción válida ingresada por el usuario.
    """
    opcion = int(input("ingrese una opcion del menu : "))
    while opcion < 0 or opcion > 11:
        opcion = int(input("ingrese nuevamente una opcion del menu : "))
    return opcion

# cargar votos 
def ingrese_votos ():
    """
    Solicita y carga los votos de los cinco partidos políticos.

    Returns:
        list: Lista con la cantidad de votos de cada partido.
    """
    votos = []
    i = 0
    while i < 5:
        partido = chr(65 + i)
        votos_añadidos = entero_no_negativo("Ingrese los votos del partido " + partido + ": ")
        votos.append(votos_añadidos)
        i = i + 1
    return votos

def cargar_votos_hardcodeados(votos):
    """Reemplaza el contenido de la lista por los votos hardcodeados.

    Returns:
        list: la misma lista con los datos hardcodeados.
    """
    funciones.limpiar_lista(votos)

    votos_partidos = [888,555,60,1850,999,777,1400,180,2500,60]

    i = 0
    while i < len(votos_partidos):
        votos.append(votos_partidos[i])
        i = i + 1
