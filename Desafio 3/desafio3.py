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
    
    return True

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
                        "fila":int(jugador[2].strip()),
                        "columna":int(jugador[3].strip()),
                        "rol":jugador[4].strip(),
                        "tiene_pelota":jugador[5].strip()
                        
                        })

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")

    return jugadores
def movimientos():
    movimientos_posibles=["arriba","abajo","izquierda","derecha"]
    print("1 - Arriba")
    print("2 - Abajo")
    print("3 - Izquierda")
    print("4 - Derecha")
    posicion=int(input("Seleccion una opción:"))
    return movimientos_posibles[posicion-11]

def mover(index,jugadores,cancha):

    jugador=jugadores[index]

    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=movimientos()
    
    match movimiento:
        case "arriba":
            cancha[fila-1][columna]=jugador["equipo"]
        case "abajo":
            cancha[fila+1][columna]=jugador["equipo"]
        case "izquierda":
            cancha[fila][columna-1]=jugador["equipo"]
        case "derecha":
            cancha[fila][columna+1]=jugador["equipo"]
        case _:
            print("Opcion no valida")
    cancha[fila][columna]="."

def mover_jugadores(jugadores,cancha):

    for index,jugador in enumerate(jugadores):
        print(f"{index } - {jugador["nombre"]}")
    jugador_index=int(input("Seleccione un jugador para mover: "))
    
    mover(jugador_index,jugadores,cancha)
    
    return True

def menu(cancha):
    continuar=True
    jugadores_registrados=False
    jugadores=[]
    
    mostrar_partido(cancha)

    while continuar:
        if not jugadores_registrados:
            print("1 - Registrar jugadores")
        print("2 - Mover jugadores en cancha")
        print("3 - Calcular distancia")
        print("4 - Detectar posibles pases")
        print("5 - Detectar posibles ofensivas")
        opcion=int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                jugadores=subir_jugadores("archivo.txt")
                jugadores_registrados = registrar_jugadores(jugadores,cancha)
            case 2:
                mover_jugadores(jugadores,cancha)
            case 3:
                print("1")
            case 4:
                print("1")
            case 5:
                print("1")
            case _:
                print("Opcion no valida")

        mostrar_partido(cancha)
    
    
    

def mostrar_partido(cancha):
        for fila in cancha:
            print("".join(fila))  

def main():

    cancha = generar_cancha()
    
    mostrar_partido(cancha)
    
    menu(cancha)
    
    

if __name__ == "__main__":
    main()