import re
def leer_archivo(archivo):
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



def cant_partidos (partidos): #Cuenta la cantidad de partidos que se dieron
    cantidad = int(len(partidos))
    return cantidad

def resultado (goles_local,goles_visita): #Revela al ganador del partido

    if goles_local > goles_visita:
        return "Local"
    if goles_local < goles_visita:
        return "Visita"
    if goles_local == goles_visita:
        return "Empate"



def tabla_de_datos (partidos): #Genera una tabla de datos en ceros
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


def puntos (info_equipos,local,visita,resultado): #Modifica la tabla de datos segun las victorias o empates
    if resultado == "Local":
        info_equipos[local]["puntos"]+=3
    if resultado == "Visita":
        info_equipos[visita]["puntos"]+=3
    if resultado == "Empate":
        info_equipos[local]["puntos"]+=1
        info_equipos[visita]["puntos"]+=1


def goles (info_equipos,local,visita,goles_local,goles_visita): #Modifica la tabla de datos segun los goles
    info_equipos[local]["goles a favor"] += goles_local
    info_equipos[local]["goles en contra"] += goles_visita
    
    info_equipos[visita]["goles a favor"] += goles_visita
    info_equipos[visita]["goles en contra"] += goles_local


def diferencia_de_goles(info_equipos,equipo): #Modifica la tabla segun sus datos ya cargados
    gf = info_equipos[equipo]["goles a favor"]
    gc = info_equipos[equipo]["goles en contra"]
    info_equipos[equipo]["diferencia de gol"] = gf - gc


def procesar_torneo(partidos):
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
        
    return info_equipos








#prints de prueba, se pueden sacar

def main():
    PARTIDOS=[]
    try:
        PARTIDOS = leer_archivo("archivo.txt")

        
        print(PARTIDOS)
        print("Cantidad de partidos")
        print(cant_partidos(PARTIDOS))
        print("Datos del torneo")
        print(procesar_torneo(PARTIDOS))
    except Exception as e:
        print("No se pudo continuar:", e)

   
main()