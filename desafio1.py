def leer_archivo(archivo):
    partidos = []

    try:
        with open(archivo, "r") as resultados_grupos:
            cant_esperada = int(resultados_grupos.readline().strip())

            for linea in resultados_grupos:
                partidos.append(linea.strip().split())

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
    




def lista_de_ceros(num):
    lista=[]
    for i in range(num):
        lista.append(0)
    return lista

def cant_partidos (partidos):
    cantidad=int(len(partidos))
    return cantidad

def tabla_de_datos (partidos,cant_datos):
    info_equipos={}
    for partido in partidos:
        local=partido[0]
        visita=partido[1]

        if local not in info_equipos:
            info_equipos[local]=lista_de_ceros(cant_datos)
        if visita not in info_equipos:
            info_equipos[visita]=lista_de_ceros(cant_datos)
    
    return info_equipos

def resultado (info_partido): #del tipo [Local,Visita,Gol. local, Gol. visita]
    if int(info_partido[2]) > int(info_partido[3]):
        return "Local"
    if int(info_partido[2]) < int(info_partido[3]):
        return "Visita"
    else:
        return "Empate"


def equipos_y_puntos (partidos):
    info_equipos=tabla_de_datos(partidos,1)

    for equipo in info_equipos:
        for partido in partidos:
            if equipo in partido:
                local=partido[0]
                visita=partido[1]

                if local == equipo:
                    if resultado(partido) == "Local":
                        info_equipos[equipo][0]+=3
                if visita == equipo:
                    if resultado(partido) == "Visita":
                        info_equipos[equipo][0]+=3
                if resultado(partido) == "Empate":
                    info_equipos[equipo][0]+=1
    return info_equipos


def desempate (partidos):
    info_equipos=tabla_de_datos(partidos,3)

    for equipo in info_equipos:
        for partido in partidos:
            if equipo in partido:
                local=partido[0]
                visita=partido[1]
                goles_local=int(partido[2])
                goles_visita=int(partido[3])

                if local == equipo:
                    info_equipos[equipo][0]+=goles_local
                    info_equipos[equipo][1]+=goles_visita
                if visita == equipo:
                    info_equipos[equipo][1]+=goles_local
                    info_equipos[equipo][0]+=goles_visita
                    
        info_equipos[equipo][2]=info_equipos[equipo][0]-info_equipos[equipo][1]
    return info_equipos


#prints de prueba, se pueden sacar

def main():
    PARTIDOS=[]
    try:
        PARTIDOS = leer_archivo("archivo.txt")

    except Exception as e:
        print("No se pudo continuar:", e)

    print(PARTIDOS)


    print(PARTIDOS)
    print("Cantidad de partidos")
    print(cant_partidos(PARTIDOS))
    print("Equipos y puntos")
    print(equipos_y_puntos(PARTIDOS))
    print("desempates")
    print(desempate(PARTIDOS))
main()