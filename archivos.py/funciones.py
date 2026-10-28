# suma de los votos totales para hacer el porcentaje total 
def votos_totales(votos):
    """
    Calcula la cantidad total de votos de todos los partidos.

    Args:
        votos (list): Lista con la cantidad de votos de cada partido.

    Returns:
        int: Cantidad total de votos.
    """
    total_votos = 0
    i = 0
    while i < len(votos):
        total_votos = total_votos + votos[i]
        i = i + 1
    return total_votos

# suma de votos
def suma_votos(votos):
    """
    Suma los valores contenidos en una lista de votos.

    Args:
        votos (list): Lista con los valores que se desean sumar.

    Returns:
        int: Resultado de la suma de los valores.
    """
    suma_de_votos = 0
    i = 0
    while i < len(votos):
        suma_de_votos = suma_de_votos + votos[i]
        i = i + 1

    return suma_de_votos

# darle las letras a los partidos politicos
def obtener_partidos(i):
    """
    Devuelve la letra correspondiente a la posición del partido.

    Args:
        i (int): Índice del partido, comenzando desde cero.

    Returns:
        str: Letra del partido correspondiente al índice.
    """
    return chr(65 + i)

def calcular_porcentaje(votos, total_votos):
    """
    Calcula el porcentaje de votos sobre el total.

    Args:
        votos (int): Cantidad de votos del partido.
        total_votos (int): Cantidad total de votos.

    Returns:
        float: Porcentaje de votos del partido.
    """
    if total_votos > 0:
        porcentaje = votos * 100 / total_votos
    else:
        porcentaje = 0

    return porcentaje

# buscar la menor cantidad de votos
def obtener_menor_votos(votos):
    """
    Busca la menor cantidad de votos de una lista.

    Args:
        votos (list): Lista con los votos de cada partido.

    Returns:
        int: La menor cantidad de votos.
    """
    menor_votos = votos[0]
    i = 1

    while i < len(votos):
        if votos[i] < menor_votos:
            menor_votos = votos[i]
        i = i + 1

    return menor_votos
