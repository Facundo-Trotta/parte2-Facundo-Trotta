# opciones del menu
def mostrar_menu():
    """ MUESTRA LA LISTA DEL MENU"""
    print("[1] Cargar Votos")
    print("[2] Mostrar Votos")
    print("[3] Partidos con menos del 10%")
    print("[4] Partidos con menos del 15%")
    print("[5] Partidos con menos del 20%")
    print("[6] Partidos con mas de 500 votos")
    print("[7] Partidos con mas de 1000 votos")
    print("[8] Partidos por encima del promedio")
    print("[9] partido menos votado")
    print("[10] Cargar votos hardcodeados")
    print("[0] Salir")

# mostrar titulo de loslistados
def titulo_listado():
    """Muestra los titulos de los resultados pedidos 
    
        Args:
            print(str): Muestra el titulo de los resultados
            
        """
    print("\n LISTADOS DE LOS PARTIDOS")
# mostrar listados
def listados(partido,votos,porcentaje):
    """Muestra en la terminar los datos de de los partidos de forma mas clara 

    Args:
        partido (str): Identificador del partido
        votos (int): Cantidad de votos recibidos
        porcentaje (float): Porcentaje de votos obtenidos
    """
    print("Partido:", partido)
    print("Cantidad de votos:", votos)
    print(f"Porcentaje de votos: {porcentaje:.2f}%")
    print()

# mostrar listados totales
def listados_totales(suma_votos, cantidad_partios, promedio ):
    """Muestra en la terminar los datos de de los partidos de forma mas clara 
    
    Args:
        partido (str): Identificador del partido
        votos (int): Cantidad de votos recibidos
        porcentaje (float): Porcentaje de votos obtenidos
    """
    print("\n LISTADO DE PARTIDOS TOTALES ")
    print("Suma de votos:", suma_votos)
    print("Cantidad de partidos:", cantidad_partios)
    print(f"Promedio de votos: {promedio:.2f}%")
    print()

# mostrar los porcentajes acomulados
def resultado_acumulado(encontrado, porcentaje_acumulado, limite):
    """
    Muestra el porcentaje acumulado o un mensaje de error.

    Args:
        encontrado (bool): Indica si se encontraron partidos.
        porcentaje_acumulado (float): Porcentaje acumulado de votos.
        limite (int): Límite de porcentaje utilizado.
    """
    if encontrado:
        print(f"Porcentaje acumulado: {porcentaje_acumulado:.2f}%")
    else:
        print("Error: no hay partidos con menos del", limite, "% de votos")

# mostrar el resultado de partidos superiores al promedio
def resultado_promedio(promedio_general, porcentaje_acumulado, encontrado):
    """
    Muestra el promedio general y el porcentaje acumulado.

    Args:
        promedio_general (float): Promedio de votos de todos los partidos.
        porcentaje_acumulado (float): Suma de los porcentajes encontrados.
        encontrado (bool): Indica si se encontraron partidos por encima
            del promedio.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    print("Promedio general de votos:",promedio_general)

    if encontrado:
        print("Porcentaje acumulado:", porcentaje_acumulado,"%")
    else:
        print("No hay partidos por encima del promedio general.")
