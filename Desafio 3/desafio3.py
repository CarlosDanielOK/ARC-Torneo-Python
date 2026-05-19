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
        print(jugador)

def subir_jugadores(archivo):

    jugadores = []

    try:
        with open(archivo, "r") as jugadores_lista:
            for linea in jugadores_lista:
                print(linea)
    
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")

    return jugadores

def menu(cancha):
    print("1 - Registrar jugadores")
    print("2 - Mover jugadores en cancha")
    print("3 - calcular distancia")
    print("4 - detectar posibles pases")
    print("5 - detectar posibles ofensivas")
    opcion=int(input("Seleccione una opcion: "))
    return opcion

def mostrar_partido(cancha):
        for fila in cancha:
            print("".join(fila))  

def main():
    cancha = generar_cancha()
    menu(cancha)
    subir_jugadores("archivo.txt")
    # mostrar_partido(cancha)

if __name__ == "__main__":
    main()