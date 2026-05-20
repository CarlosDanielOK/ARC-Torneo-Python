FILAS = 100
COLUMNAS = 60
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]

import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mensaje_ok(texto):
    print(f"\033[92m✅ {texto}\033[0m")       # verde

def mensaje_error(texto):
    print(f"\033[91m❌ {texto}\033[0m")        # rojo

def mensaje_advertencia(texto):
    print(f"\033[93m⚠️  {texto}\033[0m")      # amarillo

def mensaje_info(texto):
    print(f"\033[94mℹ️  {texto}\033[0m")      # azul

def mostrar_celda(celda):
    if celda == "A":
        return "\033[94mA\033[0m"   # azul - Argentina
    elif celda == "B":
        return "\033[93mB\033[0m"   # amarillo - Brasil  
    elif celda == "X":
        return "\033[91mX\033[0m"   # rojo - obstáculo
    else:
        return "."
def pedir_input(mensaje):
    return input(f"\033[96m  ➜  {mensaje}\033[0m ")

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

def mostrar_menu_movimientos(jugador):
    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print(f"║  Moviendo: {jugador['nombre']:<34}║")
    print(f"║  Posición: Fila {jugador['fila']:<3} Columna {jugador['columna']:<17}║")
    print("╠══════════════════════════════════════════════╣")
    print("║              1 - ⬆  Arriba                   ║")
    print("║              2 - ⬇  Abajo                    ║")
    print("║              3 - ⬅  Izquierda                ║")
    print("║              4 - ➡  Derecha                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║              0 - Cancelar                    ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

def movimientos(jugador):

    movimientos_posibles=["arriba","abajo","izquierda","derecha"]
    
    mostrar_menu_movimientos(jugador)

    posicion=int(pedir_input("Seleccion una opción:"))
    
    return movimientos_posibles[posicion-1]

def mover(index,jugadores,cancha):

    jugador=jugadores[index]

    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=movimientos(jugador)
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
def mostrar_lista_jugadores(jugadores):
    print("\033[96m")
    print("╔════════════════════════════════════════════════╗")
    print("║             SELECCIONAR JUGADOR                ║")
    print("╠══════╦══════════════╦═════════╦════════════════╣")
    print("║  N°  ║    Nombre    ║  Equipo ║      Rol       ║")
    print("╠══════╬══════════════╬═════════╬════════════════╣")
    for index, jugador in enumerate(jugadores):
        pelota = "⚽" if jugador["tiene_pelota"] == "True" else "  "
        print(f"║  {index+1:<3} ║ {jugador['nombre']:<12} ║   {jugador['equipo']}  {pelota} ║ {jugador['rol']:<14} ║")
    print("╠══════╩══════════════╩═════════╩════════════════╣")
    print("║  0 - Cancelar                                  ║")
    print("╚════════════════════════════════════════════════╝")
    print("\033[0m")

def mover_jugadores(jugadores,cancha):

    se_movio = False
    
    mostrar_lista_jugadores(jugadores)

    jugador_index=int(pedir_input("Seleccione un jugador para mover: "))-1
    
    if jugador_index == -1:
        return True  # salir sin mover
    try:
        se_movio = mover(jugador_index,jugadores,cancha)
    except Exception as e:
        print(e)
    
    return se_movio

def mostrar_menu():
    print("\033[96m")  # cian
    print("╔══════════════════════════════╗")
    print("║     LA CANCHA INTELIGENTE    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Registrar jugadores      ║")
    print("║  2. Mover jugador            ║")
    print("║  3. Distancia a la pelota    ║")
    print("║  4. Detectar pases           ║")
    print("║  5. Camino libre al arco     ║")
    print("║  0. Salir                    ║")
    print("╚══════════════════════════════╝")
    print("\033[0m")

def menu(cancha):
    continuar=True
    jugadores_registrados=False
    jugadores=[]

    limpiar_pantalla()  
    mostrar_partido(cancha)

    while continuar:
        # if not jugadores_registrados:
        
        mostrar_menu()

        opcion=int(pedir_input("Seleccione una opcion: "))

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
        limpiar_pantalla()
        mostrar_partido(cancha)
    
    
    

def mostrar_partido(cancha):
        for fila in cancha:
            print("".join(mostrar_celda(celda) for celda in fila))

def main():

    cancha = generar_cancha()
    
    mostrar_partido(cancha)
    
    menu(cancha)
    
    

if __name__ == "__main__":
    main()