FILAS = 100
COLUMNAS = 60
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]


def generar_cancha():
    cancha = []
    for fila in range(FILAS):
        fila_nueva = []
        for columna in range(COLUMNAS):
            fila_nueva.append(".")
        cancha.append(fila_nueva)
    return cancha

def registrar_jugadores(jugadores,cancha):
    for jugador in jugadores:
        cancha[int(jugador["fila"])][int(jugador["columna"])]=jugador["equipo"]

def subir_jugadores(archivo):

    jugadores = []

    try:
        with open(archivo, "r") as jugadores_lista:
            for linea in jugadores_lista:
                jugador=linea.split("|")
                jugadores.append(
                    {
                        "nombre":jugador[0].strip(),
                        "equipo":jugador[1].strip(),
                        "fila":jugador[2].strip(),
                        "columna":jugador[3].strip(),
                        "rol":jugador[4].strip(),
                        "tiene_pelota":jugador[5].strip()
                        
                        })

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")

    return jugadores

def menu(cancha):
    continuar=True
    while continuar:
        if jugadores:
            print("1 - Registrar jugadores")
        print("2 - Mover jugadores en cancha")
        print("3 - Calcular distancia")
        print("4 - Detectar posibles pases")
        print("5 - Detectar posibles ofensivas")
        opcion=int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                jugadores=subir_jugadores("archivo.txt")
            case 2:
                print("1")
            case 3:
                print("1")
            case 4:
                print("1")
            case 5:
                print("1")
            case _:
                print("Opcion no valida")
            
        registrar_jugadores(jugadores,cancha)
    

def mostrar_partido(cancha):
        for fila in cancha:
            print("".join(fila))  

def main():

    cancha = generar_cancha()
    
    mostrar_partido(cancha)
    
    menu(cancha)
    
    mostrar_partido(cancha)
    

if __name__ == "__main__":
    main()