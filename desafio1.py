import re
def leer_archivo(archivo):
    """
    Lee y procesa el archivo de texto con los resultados de los partidos.
    Utiliza validación por expresiones regulares para asegurar el formato correcto.

    Args:
        archivo (str): Ruta del archivo a leer.

    Returns:
        list: Lista donde cada elemento es a su vez una lista con los datos de un partido.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato o la cantidad de partidos es incorrecta.
    """
    partidos = []

    try:
        with open(archivo, "r") as resultados_grupos:
            try:
                cant_esperada = int(resultados_grupos.readline().strip())
            except ValueError:
                raise ValueError("La primera línea debe ser la cantidad de partidos")

            if cant_esperada != 6:
                raise ValueError(f"Se esperaban 6 partidos, el archivo indica {cant_esperada}")

            patron = r"^([A-Z]{3}) (?!\1)[A-Z]{3} (?:[0-9]|1[0-9]|20) (?:[0-9]|1[0-9]|20)$"
            for linea in resultados_grupos:
                linea_strip=linea.strip()
                if re.match(patron, linea_strip):
                    partidos.append(linea_strip.split())
                else:
                    raise ValueError("Error en datos del archivo, partidos mal ingresados")

            cant_real = len(partidos)
            if cant_real != cant_esperada:
                raise ValueError(
                    "Cantidad incorrecta de partidos: esperados 6 partidos"
                )
        return partidos

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")


def resultado(goles_local, goles_visita):
    """
    Compara los goles y revela al ganador del partido o si hubo empate.

    Args:
        goles_local (int): Goles del equipo de casa.
        goles_visita (int): Goles del equipo visitante.

    Returns:
        str: 'Local', 'Visita' o 'Empate'.
    """
    if goles_local > goles_visita:
        return "Local"
    if goles_local < goles_visita:
        return "Visita"
    if goles_local == goles_visita:
        return "Empate"


def tabla_de_datos(partidos):
    """
    Genera un diccionario base con todos los equipos en cero.
    Se utiliza .copy() para evitar que todos los equipos referencien al mismo diccionario en memoria,
    lo cual sería un error donde cambiar a uno cambiaría a todos.

    Args:
        partidos (list): Lista de todos los partidos.

    Returns:
        dict: Tabla inicial de todos los equipos.
    """
    info_equipos = {}

    for partido in partidos:
        local = partido[0]
        visita = partido[1]
        estadisticas_vacias={
            "puntos":0,
            "goles a favor":0,
            "goles en contra":0,
            "diferencia de gol":0,
            "partidos jugados":0
        }

        if local not in info_equipos:
            info_equipos[local] = estadisticas_vacias.copy()
        if visita not in info_equipos:
            info_equipos[visita] = estadisticas_vacias.copy()
    if len(info_equipos)!=4:raise ValueError("Cantidad de equipos erronea , verificar que sean 4 equipos")
    return info_equipos


def partidos_jugados(info_equipos, local, visita):
    """
    Modifica la tabla de datos sumando 1 por cada partido en el que participe el equipo.

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.
        local (str): Nombre del equipo local.
        visita (str): Nombre del equipo visitante.
    """
    info_equipos[local]["partidos jugados"] += 1
    info_equipos[visita]["partidos jugados"] += 1


def puntos(info_equipos, local, visita, resultado):
    """
    Modifica la tabla de datos asignando puntos según las victorias (3) o empates (1).

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.
        local (str): Nombre del equipo local.
        visita (str): Nombre del equipo visitante.
        resultado (str): Cadena indicando el ganador ("Local", "Visita", "Empate").
    """
    if resultado == "Local":
        info_equipos[local]["puntos"]+=3
    if resultado == "Visita":
        info_equipos[visita]["puntos"]+=3
    if resultado == "Empate":
        info_equipos[local]["puntos"]+=1
        info_equipos[visita]["puntos"]+=1


def goles(info_equipos, local, visita, goles_local, goles_visita):
    """
    Modifica la tabla de datos sumando los goles a favor y en contra de ambos equipos.

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.
        local (str): Nombre del equipo local.
        visita (str): Nombre del equipo visitante.
        goles_local (int): Goles del equipo local.
        goles_visita (int): Goles del equipo visitante.
    """
    info_equipos[local]["goles a favor"] += goles_local
    info_equipos[local]["goles en contra"] += goles_visita
    
    info_equipos[visita]["goles a favor"] += goles_visita
    info_equipos[visita]["goles en contra"] += goles_local


def diferencia_de_goles(info_equipos, equipo):
    """
    Calcula y almacena la diferencia de goles de un equipo (GF - GC).

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.
        equipo (str): Nombre del equipo a actualizar.
    """
    gf = info_equipos[equipo]["goles a favor"]
    gc = info_equipos[equipo]["goles en contra"]
    info_equipos[equipo]["diferencia de gol"] = gf - gc


def nombre_equipo(info_equipo):
    """
    Retorna el nombre del equipo.

    Args:
        info_equipo (tuple): Tupla con el nombre del equipo y sus estadísticas.

    Returns:
        string: Nombre de equipo
    """
    return info_equipo[0]


def info_determinante(info_equipo):
    """
    Retorna los datos clave que determinan la clasificación oficial.
    Este paso permite usar una tupla para aplicar los múltiples criterios de desempate en orden.

    Args:
        info_equipo (tuple): Tupla con el nombre del equipo y sus estadísticas.

    Returns:
        tuple: (puntos, diferencia de gol, goles a favor, nombre_equipo)
    """
    datos = info_equipo[1]

    return (datos["puntos"],datos["diferencia de gol"],datos["goles a favor"])


def clasificacion(info_equipos):
    """
    Ordena completamente los equipos basándose en los factores determinantes (Puntos, Diferencia de goles, Goles a favor).
    En caso de empate numerico se matendra el primer ordenamiento por nombre alfabeticamente.

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.

    Returns:
        list: Lista de tuplas completamente ordenada de primero a último.
    """
    lista_equipos = list(info_equipos.items())

    lista_equipos = sorted(lista_equipos,key = nombre_equipo)
    lista_equipos = sorted(lista_equipos,key = info_determinante,reverse = True)

    return lista_equipos


def procesar_torneo(partidos):
    """
    Función principal que genera la tabla, itera sobre los partidos y asienta los puntos y goles.
    Calcula al final la diferencia de gol y devuelve el diccionario de equipos ordenados.

    Args:
        partidos (list): Lista de partidos procesada por leer_archivo.

    Returns:
        dict: Diccionario final ordenado (actualmente por puntos).
    """
    info_equipos = tabla_de_datos(partidos)
    for partido in partidos:
        local = partido[0]
        visita = partido[1]
        goles_local = int(partido[2])
        goles_visita = int(partido[3])
        res = resultado(goles_local,goles_visita)

        puntos(info_equipos,local,visita,res)

        goles(info_equipos,local,visita,goles_local,goles_visita)

        partidos_jugados(info_equipos,local,visita)

    for equipo in info_equipos:
        diferencia_de_goles(info_equipos,equipo)
        
    return clasificacion(info_equipos)


def mostrar_resultados(equipos):
    """
    Imprime en pantalla los clasificados respetando estrictamente el 
    formato requerido (renglones sin espacios adicionales).

    Args:
        equipos (list): Lista de todos los equipos del torneo ordenados.
    """
    print("Clasificados:")
    print(equipos[0][0])
    print(equipos[1][0])
    print("Tercero:")
    print(equipos[2][0])


def mensaje_salida():
    respuesta = input("¿Desea salir? (s/n): ")
    if respuesta.lower() != "n":
        print("Saliendo...")
        return True
    return False


def main():
    while True:
        try:
            ruta_archivo = input("Ingrese la direccion del archivo: ")
            mostrar_resultados(procesar_torneo(leer_archivo(ruta_archivo)))
        except Exception as e:
            print(f"Error: {e}")
        
        if mensaje_salida():
            break

main()
