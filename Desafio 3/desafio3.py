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
    
    if jugador["rol"] in ROLES_VALIDOS:
        valido = True
    if jugador["equipo"] in EQUIPOS_VALIDOS:
        valido = True
    if 0 <= jugador["fila"] < FILAS:
        valido = True
    if 0 <= jugador["columna"] < COLUMNAS:
        valido = True
    for jugador_posicionado in jugadores:
        if jugador_posicionado['fila'] == jugador["fila"] and jugador_posicionado['columna'] == jugador["columna"]:
            valido=False 
        if jugador_posicionado['tiene_pelota']=="True" and jugador["tiene_pelota"]=="True":
            valido=False   
    return valido    

def registrar_jugador(jugador,jugadores):
    
    valido=validar_jugador(jugador,jugadores)
    if valido:
        jugadores.append(jugador)

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

def elegir_movimientos(jugador):

    movimientos_posibles=["arriba","abajo","izquierda","derecha"]
    
    mostrar_menu_movimientos(jugador)

    direccion=int(pedir_input("Seleccion una opción:"))
    
    return movimientos_posibles[direccion-1]

def mover(jugador,cancha):

    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=elegir_movimientos(jugador)

    se_movio=False
    match movimiento:
        case "arriba":
            if fila-1 >= 0 and cancha[fila+1][columna]=='.' :
                print("arriba")
                cancha[fila-1][columna]=jugador["equipo"]
                jugador["fila"]=fila-1
                se_movio=True
            else: 
                raise IndexError("No se puede mover a esa posicion")
        case "abajo":
            if fila< FILAS and cancha[fila+1][columna]=='.':
                cancha[fila+1][columna]=jugador["equipo"]
                jugador["fila"]=fila+1
                se_movio=True
            else:
                raise IndexError("No se puede mover a esa pocision")
        case "izquierda":
            if columna-1 >= 0 and cancha[fila][columna-1]=='.':
                cancha[fila][columna-1]=jugador["equipo"]
                jugador["columna"]=columna-1
                se_movio=True
            else: 
                raise IndexError("No se puede mover a esa pocision")
        case "derecha":
            if columna+1< 60 and cancha[fila][columna+1]=='.':
                cancha[fila][columna+1]=jugador["equipo"]
                jugador["columna"]=columna+1
                se_movio=True
            else:
                mensaje_error("Movimiento inválido")
            return False

        case _:
            se_movio=False
            print("Opcion no valida")
    if se_movio:
        cancha[fila][columna]="."

    return se_movio
    
def mostrar_lista_jugadores(jugadores):
    print("\033[96m")
    
    print("╔══════╦══════════════╦═════════╦════════════════╦═══════╦══════════╗")
    print("║  N°  ║    Nombre    ║ Equipo  ║      Rol       ║ Fila  ║ Columna  ║")
    print("╠══════╬══════════════╬═════════╬════════════════╬═══════╬══════════╣")

    for index, jugador in enumerate(jugadores):

        pelota = "⚽" if jugador["tiene_pelota"] == "True" else "  "

        print(
            f"║ {index+1:<4} ║ "
            f"{jugador['nombre']:<12} ║ "
            f"  {jugador['equipo']} {pelota}  ║ "
            f"{jugador['rol']:<14} ║ "
            f"{jugador['fila']:<5} ║ "
            f"{jugador['columna']:<8} ║"
        )

    print("╠══════╩══════════════╩═════════╩════════════════╩═══════╩══════════╣")
    print("║  0 - Cancelar                                                     ║")
    print("╚═══════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

def menu_mover_jugadores(jugadores,cancha):

    se_movio = False
    
    mostrar_lista_jugadores(jugadores)

    jugador_index=int(pedir_input("Seleccione un jugador para mover: "))-1
    
    if jugador_index < 0:
            se_movio=True
    else:
        try:
            jugador_seleccionado=jugadores[jugador_index]
            se_movio = mover(jugador_seleccionado,cancha)
        except Exception as e:
                print(e)
        
    return se_movio

def mover_jugadores(jugadores,cancha):
    se_movio=False
    while not se_movio:
        se_movio = menu_mover_jugadores(jugadores,cancha)  
    
def opcion_registrar_jugadores(jugadores,cancha):
    
    jugadores_archivo=subir_jugadores("archivo.txt")
    
    for jugador in jugadores_archivo:
        registrar_jugador(jugador,jugadores)



    jugadores_registrados = registrar_jugadores(jugadores,cancha)

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

def controlador_opciones(cancha,jugadores):
    continuar=True
    while continuar:
        # if not jugadores_registrados:
        
        mostrar_menu()

        opcion=int(pedir_input("Seleccione una opcion: "))

        match opcion:
            case 1:
                opcion_registrar_jugadores(jugadores,cancha)
            case 2:
                mover_jugadores(jugadores,cancha)         
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


def menu(cancha):
    
    jugadores=[]

    limpiar_pantalla()  
    mostrar_partido(cancha)

    controlador_opciones(cancha, jugadores)
    
    
    

def mostrar_partido(cancha):
        print(" ", end="")

        for columna in range(COLUMNAS+1):
            print(f"{columna:<3}", end="")

        print()
        for index,fila in enumerate(cancha):
            print(f"{index+1:<4}",end="")
            print(f"{"":<2}".join(mostrar_celda(celda) for celda in fila))

def main():

    cancha = generar_cancha()
    
    mostrar_partido(cancha)
    
    menu(cancha)
    
    

if __name__ == "__main__":
    main()