# importo los datos de los otros archivos a este 
import salidas
import entradas
import funciones

# mostramos los votos
def mostrar_votos(votos):
    """
    Muestra la cantidad de votos y el porcentaje de cada partido.

    Args:
        votos (list): Lista con los votos de cada partido.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    total_votos = funciones.votos_totales(votos) 
    i = 0
    salidas.titulo_listado()

    while i < len(votos):
        partido = funciones.obtener_partidos(i)
        if total_votos > 0:
            porcentaje = votos[i] * 100 / total_votos
        else:
            porcentaje = 0
        salidas.listados(partido, votos[i], porcentaje)
        i = i + 1

# mostrar los porcentajes pedidos de menor cantidad
def mostrar_porcentaje_menor(votos, limite):
    """
    Muestra los partidos cuyo porcentaje de votos es menor al límite
    y calcula el porcentaje acumulado de los resultados encontrados.

    Args:
        votos (list): Lista con los votos de cada partido.
        limite (int): Porcentaje máximo que deben cumplir los partidos.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    total_votos = funciones.votos_totales(votos)
    salidas.titulo_listado()

    porcentaje_acumulado = 0
    encontrado = False
    i = 0
    while i < len(votos):
        partido = funciones.obtener_partidos(i)
        porcentaje = funciones.calcular_porcentaje(votos[i], total_votos)
        if porcentaje < limite:
            salidas.listados(partido, votos[i], porcentaje)
            porcentaje_acumulado = porcentaje_acumulado + porcentaje
            encontrado = True
        i = i + 1
    salidas.resultado_acumulado(encontrado, porcentaje_acumulado, limite)


# los partidos mas votados segun el parametro puesto como limite
def mostrar_mas_votos(votos, limite):
    """
    Muestra los partidos que alcanzan o superan el límite de votos
    y calcula la suma y el promedio de los partidos seleccionados.

    Args:
        votos (list): Lista con los votos de cada partido.
        limite (int): Cantidad mínima de votos requerida.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    total_votos = funciones.votos_totales(votos)
    salidas.titulo_listado()
    datos_filtrados = []
    suma_votos = 0
    cantidad_partidos = 0
    i = 0
    while i < len(votos):
        if votos[i] >= limite:
            partido = funciones.obtener_partidos(i)
            porcentaje = funciones.calcular_porcentaje(votos[i], total_votos)
            salidas.listados(partido, votos[i], porcentaje)
            datos_filtrados.append(votos[i])
            cantidad_partidos = cantidad_partidos + 1
        i = i + 1
    if cantidad_partidos > 0:
        suma_votos = funciones.suma_votos(datos_filtrados)
        promedio = suma_votos / cantidad_partidos
        salidas.listados_totales(suma_votos ,cantidad_partidos,promedio)
    else:
        print("Error: no hay partidos con más de", limite, "votos")

# mostrar promedio
def mostrar_promedio(votos):
    """
    Muestra los partidos que superan el promedio general de votos.
    También muestra el promedio general y el porcentaje acumulado.

    Args:
        votos (list): Lista con los votos de cada partido.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    total_votos = funciones.votos_totales(votos)
    promedio_general = total_votos / len(votos)
    porcentaje_acumulado = 0
    encontrado = False
    i = 0

    salidas.titulo_listado()

    while i < len(votos):
        partido = funciones.obtener_partidos(i)
        porcentaje = funciones.calcular_porcentaje(votos[i], total_votos)

        if votos[i] > promedio_general:
            salidas.listados(partido, votos[i], porcentaje)
            porcentaje_acumulado = porcentaje_acumulado + porcentaje
            encontrado = True

        i = i + 1

    salidas.resultado_promedio(promedio_general, porcentaje_acumulado, encontrado)

# mostrar el menor numero
def partido_menor(votos):
    """
    Muestra todos los partidos que tienen la menor cantidad de votos.

    Args:
        votos (list): Lista con los votos de cada partido.

    Returns:
        None: Muestra los resultados por pantalla.
    """
    if len(votos) == 0:
        print("Error: no hay votos cargados.")
        return

    menor_votos = votos[0]
    i = 1

    menor_votos = funciones.obtener_menor_votos(votos)

    # Mostramos todos los partidos que tienen esa cantidad
    total_votos = funciones.votos_totales(votos)
    salidas.titulo_listado()

    i = 0
    while i < len(votos):
        if votos[i] == menor_votos:
            partido = funciones.obtener_partidos(i)
            porcentaje = funciones.calcular_porcentaje(
                votos[i], total_votos
            )
            salidas.listados(partido, votos[i], porcentaje)

        i = i + 1


#ejecuta el manu
def ejecutar_menu():
    """
    Ejecuta el menú principal y permite seleccionar las operaciones
    del sistema electoral.

    Returns:
        None: Controla la ejecución del programa mediante el menú.
    """
    votos = []
    datos_agregados = False
    opcion = -1
    while opcion !=-0:
        salidas.mostrar_menu()
        opcion = entradas.ingresar_opcion()
        if opcion == 0:
            print("=== Hasta la proxima y espero que te alla gustado el sitio ===")
            pass
        elif opcion == 1:
            votos = entradas.ingrese_votos()
            datos_agregados = True
        elif not datos_agregados:
            print("primero debes cargar los datos")
        elif opcion == 2:
            mostrar_votos(votos)
        elif opcion == 3:
            mostrar_porcentaje_menor(votos, 10)
        elif opcion == 4:
            mostrar_porcentaje_menor(votos, 15)
        elif opcion == 5:
            mostrar_porcentaje_menor(votos, 20)
        elif opcion == 6:
            mostrar_mas_votos(votos, 500)
        elif opcion == 7:
            mostrar_mas_votos(votos, 1000)
        elif opcion == 8:
            mostrar_promedio(votos)
        elif opcion == 9:
            partido_menor(votos)
        elif opcion == 10:
            entradas.cargar_votos_hardcodeados(votos)
        




