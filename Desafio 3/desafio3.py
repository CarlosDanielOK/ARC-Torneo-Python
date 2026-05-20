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
        cancha[jugador["fila"]][jugador["columna"]]=jugador["equipo"]
            
    return True

def validar_jugador(jugador,jugadores):
    valido=False
    if jugador["rol"] is ROLES_VALIDOS:
        valido = True
    if jugador["equipo"] is EQUIPOS_VALIDOS:
        valido = True
    if 0 < jugador["fila"] < 100:
        valido = True
    if 0 < jugador["columna"] < 60:
        valido = True
    for jugador_posicionado in jugadores:
        if jugador_posicionado['fila'] == jugador["fila"] and jugador_posicionado['columna'] == jugador["columna"]:
            valido=False 
        if jugador_posicionado['tiene_pelota']=="True" and jugador["tiene_pelota"]=="True":
            valido=False   
    return valido    

def subir_jugadores(archivo):

    jugadores = []

    try:
        with open(archivo, "r") as jugadores_lista:
            for linea in jugadores_lista:
                jugador=linea.split("|")

                jugador = {
                        "nombre":jugador[0].strip(),
                        "equipo":jugador[1].strip(),
                        "fila":int(jugador[2].strip()),
                        "columna":int(jugador[3].strip()),
                        "rol":jugador[4].strip(),
                        "tiene_pelota":jugador[5].strip()
                        }
                valido = validar_jugador(jugador,jugadores)


 
                if valido:
                    jugadores.append(jugador)

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")

    return jugadores
def movimientos():

    movimientos_posibles=["arriba","abajo","izquierda","derecha"]
    
    for index,movs in enumerate(movimientos_posibles):
        print(f"{index+1} - {movs}")

    posicion=int(input("Seleccion una opción:"))
    
    return movimientos_posibles[posicion-1]

def mover(index,jugadores,cancha):

    jugador=jugadores[index]

    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=movimientos()
    se_movio=False

    match movimiento:
        case "arriba":
            if fila-1 >= 0 and not cancha[fila-1][columna] in EQUIPOS_VALIDOS :
                print("arriba")
                cancha[fila-1][columna]=jugador["equipo"]
                jugador["fila"]=fila-1
                se_movio=True
            else: 
                raise IndexError("No se puede mover a esa posicion")
        case "abajo":
            if fila< 100 and not cancha[fila+1][columna] in EQUIPOS_VALIDOS and cancha[fila+1][columna]=='.':
                cancha[fila+1][columna]=jugador["equipo"]
                jugador["fila"]=fila+1
                se_movio=True
            else:
                raise IndexError("No se puede mover a esa pocision")
        case "izquierda":
            if columna-1 >= 0 and not cancha[fila][columna-1] in EQUIPOS_VALIDOS and cancha[fila][columna-1]=='.':
                cancha[fila][columna-1]=jugador["equipo"]
                jugador["columna"]=columna-1
                se_movio=True
            else: 
                raise IndexError("No se puede mover a esa pocision")
        case "derecha":
            if columna+1< 60 and not cancha[fila][columna+1] in EQUIPOS_VALIDOS and cancha[fila][columna+1]=='.':
                cancha[fila][columna+1]=jugador["equipo"]
                jugador["columna"]=columna+1
                se_movio=True
            else:
                raise IndexError("No se puede mover a esa pocision")

        case _:
            se_movio=False
            print("Opcion no valida")
    if se_movio:
        cancha[fila][columna]="."

    return se_movio

def mover_jugadores(jugadores,cancha):

    se_movio = False
    for index,jugador in enumerate(jugadores):
        print(f"{index+1} - {jugador["nombre"]}")
    jugador_index=int(input("Seleccione un jugador para mover: "))-1
    try:
        se_movio = mover(jugador_index,jugadores,cancha)
    except Exception as e:
        print(e)
    
    return se_movio

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
        print("0 - Salir")
        opcion=int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                jugadores=subir_jugadores("archivo.txt")
                jugadores_registrados = registrar_jugadores(jugadores,cancha)
            case 2:
                se_movio=False
                while not se_movio:
                    se_movio =mover_jugadores(jugadores,cancha)
                
            case 3:
                print("1")
            case 4:
                print("1")
            case 5:
                print("1")
            case _:
                continuar=False

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