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
            cant_esperada = int(resultados_grupos.readline().strip())


            patron = r"^[A-Z]{3} [A-Z]{3} \d+ \d+$"

            for linea in resultados_grupos:
                if re.match(patron, linea):
                    partidos.append(linea.strip().split())
                else:
                    raise ValueError("Error en datos del archivo, partidos mal ingresados")

        cant_real = len(partidos)

        if cant_real != cant_esperada:
            raise ValueError(
                f"Cantidad incorrecta de partidos: esperados {cant_esperada}, encontrados {cant_real}"
            )

        print("Archivo leido correctamente")

        return partidos

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")

    except ValueError:
        raise ValueError("Error en datos del archivo")



def cant_partidos(partidos):
    """
    Cuenta la cantidad de partidos que se procesaron.

    Args:
        partidos (list): Lista con los resultados.

    Returns:
        int: El total de partidos.
    """
    cantidad = int(len(partidos))
    return cantidad

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
            "diferencia de gol":0
        }

        if local not in info_equipos:
            info_equipos[local] = estadisticas_vacias.copy()
        if visita not in info_equipos:
            info_equipos[visita] = estadisticas_vacias.copy()
    return info_equipos


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

    for equipo in info_equipos:
        diferencia_de_goles(info_equipos,equipo)
        
    return clasificacion(info_equipos)

def info_determinante(info_equipo):
    """
    Retorna los datos clave que determinan la clasificación oficial.
    Este paso permite usar una tupla para aplicar los múltiples criterios de desempate en orden.

    Args:
        info_equipo (tuple): Tupla con el nombre del equipo y sus estadísticas.

    Returns:
        tuple: (puntos, diferencia de gol, goles a favor, nombre_equipo)
    """
    equipo = info_equipo[0]
    datos = info_equipo[1]
    puntos = datos["puntos"]
    dg = datos["diferencia de gol"]
    gf = datos["goles a favor"]

    return (puntos,dg,gf,equipo)

def clasificacion(info_equipos):
    """
    Ordena completamente los equipos basándose en los factores determinantes (Puntos, DG, GF).

    Args:
        info_equipos (dict): Diccionario principal con las estadísticas.

    Returns:
        list: Lista de tuplas completamente ordenada de primero a último.
    """
    return sorted(info_equipos.items(),key=info_determinante,reverse = True)








#prints de prueba, se pueden sacar

def mostrar_resultados(equipos):
    """
    Imprime en pantalla la lista de los clasificados respetando estrictamente el 
    formato requerido (renglones sin espacios adicionales).

    Args:
        equipos (list): Lista de todos los equipos del torneo ordenados.
    """
    # Extrae solo los nombres de la lista de tuplas (o diccionario)
    nombres = []
    for equipo in equipos:
        if isinstance(equipo, tuple):
            nombres.append(equipo[0]) # Si es tupla, el nombre está en la primera posición
        else:
            nombres.append(equipo)    # Si pasaron una lista de strings o claves de un dict

    print("Clasificados:")
    print(nombres[0])
    print(nombres[1])
    print("Tercero:")
    print(nombres[2])


def main():
    PARTIDOS=[]
    try:
        PARTIDOS = leer_archivo("archivo.txt")

        equipos = list(procesar_torneo(PARTIDOS))
        mostrar_resultados(equipos)

    except Exception as e:
        print("No se pudo continuar:", e)

   
main()