FILAS = 40
COLUMNAS = 60
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]
JUGADORES = [
    {
        "nombre": "Romero",
        "equipo": "A",
        "fila": 20,
        "columna": 2,
        "rol": "arquero",
        "tiene_pelota": False
    },
    {
        "nombre": "Otamendi",
        "equipo": "A",
        "fila": 12,
        "columna": 8,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Lisandro",
        "equipo": "A",
        "fila": 20,
        "columna": 10,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Tagliafico",
        "equipo": "A",
        "fila": 28,
        "columna": 12,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Molina",
        "equipo": "A",
        "fila": 6,
        "columna": 15,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "DePaul",
        "equipo": "A",
        "fila": 14,
        "columna": 20,
        "rol": "mediocampista",
        "tiene_pelota": True
    },
    {
        "nombre": "MacAllister",
        "equipo": "A",
        "fila": 20,
        "columna": 22,
        "rol": "mediocampista",
        "tiene_pelota": False
    },
    {
        "nombre": "Fernandez",
        "equipo": "A",
        "fila": 26,
        "columna": 25,
        "rol": "mediocampista",
        "tiene_pelota": False
    },
    {
        "nombre": "DiMaria",
        "equipo": "A",
        "fila": 8,
        "columna": 27,
        "rol": "delantero",
        "tiene_pelota": False
    },
    {
        "nombre": "Messi",
        "equipo": "A",
        "fila": 16,
        "columna": 29,
        "rol": "delantero",
        "tiene_pelota": False
    },
    {
        "nombre": "Alvarez",
        "equipo": "A",
        "fila": 18,
        "columna": 31,
        "rol": "delantero",
        "tiene_pelota": False
    },
    {
        "nombre": "Alisson",
        "equipo": "B",
        "fila": 20,
        "columna": 57,
        "rol": "arquero",
        "tiene_pelota": False
    },
    {
        "nombre": "Marquinhos",
        "equipo": "B",
        "fila": 12,
        "columna": 52,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Silva",
        "equipo": "B",
        "fila": 20,
        "columna": 50,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Militao",
        "equipo": "B",
        "fila": 28,
        "columna": 48,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Danilo",
        "equipo": "B",
        "fila": 6,
        "columna": 45,
        "rol": "defensor",
        "tiene_pelota": False
    },
    {
        "nombre": "Casemiro",
        "equipo": "B",
        "fila": 14,
        "columna": 40,
        "rol": "mediocampista",
        "tiene_pelota": False
    },
    {
        "nombre": "Paqueta",
        "equipo": "B",
        "fila": 20,
        "columna": 38,
        "rol": "mediocampista",
        "tiene_pelota": False
    },
    {
        "nombre": "Gomes",
        "equipo": "B",
        "fila": 26,
        "columna": 35,
        "rol": "mediocampista",
        "tiene_pelota": False
    },
    {
        "nombre": "Raphinha",
        "equipo": "B",
        "fila": 8,
        "columna": 33,
        "rol": "delantero",
        "tiene_pelota": False
    },
    {
        "nombre": "Rodrygo",
        "equipo": "B",
        "fila": 18,
        "columna": 32,
        "rol": "delantero",
        "tiene_pelota": False
    },
    {
        "nombre": "Neymar",
        "equipo": "B",
        "fila": 38,
        "columna": 30,
        "rol": "delantero",
        "tiene_pelota": False
    }
]

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

def posicionar_jugador(jugador,cancha):
        cancha[jugador["fila"]][jugador["columna"]]=jugador["equipo"]
            
# def validar_jugador(jugador,jugadores):
    
#     valido=False
    
#     if jugador["rol"] in ROLES_VALIDOS:
#         valido = True
#     if jugador["equipo"] in EQUIPOS_VALIDOS:
#         valido = True
#     if 0 <= jugador["fila"] < FILAS:
#         valido = True
#     if 0 <= jugador["columna"] < COLUMNAS:
#         valido = True
#     for jugador_posicionado in jugadores:
#         if jugador_posicionado['fila'] == jugador["fila"] and jugador_posicionado['columna'] == jugador["columna"]:
#             valido=False 
#         if jugador_posicionado['tiene_pelota'] and jugador["tiene_pelota"]:
#             valido=False   
#     return valido    

# def registrar_jugador(jugador,jugadores):
    
#     valido=validar_jugador(jugador,jugadores)
#     if valido:
#         jugadores.append(jugador)

#     return valido    

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
    movimiento="cancelar"
    mostrar_menu_movimientos(jugador)

    direccion=int(pedir_input("Seleccion una opción:"))
    if direccion > 0:
        movimiento=movimientos_posibles[direccion-1]

    return movimiento

def mover(jugador,cancha):

    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=elegir_movimientos(jugador)

    se_movio=False
    match movimiento:
        case "arriba":
            if fila-1 >= 0 and cancha[fila-1][columna]=='.' :
                print("arriba")
                cancha[fila-1][columna]=jugador["equipo"]
                jugador["fila"]=fila-1
                se_movio=True
            else: 
                raise IndexError("No se puede mover a esa posicion")
        case "abajo":
            if fila+1< FILAS and cancha[fila+1][columna]=='.':
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
            if columna+1< COLUMNAS and cancha[fila][columna+1]=='.':
                cancha[fila][columna+1]=jugador["equipo"]
                jugador["columna"]=columna+1
                se_movio=True
            else:
                raise IndexError("No se puede mover a esa pocision")
        case _:
            raise print()
    if se_movio:
        cancha[fila][columna]="."

    return se_movio
    
def lista_jugadores(jugadores):
    print("\033[96m")
    
    print("╔══════╦══════════════╦═════════╦════════════════╦═══════╦══════════╗")
    print("║  N°  ║    Nombre    ║ Equipo  ║      Rol       ║ Fila  ║ Columna  ║")
    print("╠══════╬══════════════╬═════════╬════════════════╬═══════╬══════════╣")

    for index, jugador in enumerate(jugadores):

        pelota = "⚽" if jugador["tiene_pelota"] else "  "

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
    
    lista_jugadores(jugadores)

    jugador_index=int(pedir_input("Seleccione un jugador para mover: "))-1
    
    if jugador_index < 0:
            se_movio=True
    else:
        try:
            jugador_seleccionado=jugadores[jugador_index]
            se_movio = mover(jugador_seleccionado,cancha)
        except Exception as e:
                mensaje_error("Opxion invalida")
        
    return se_movio

def mover_jugadores(jugadores,cancha):
    se_movio=False
    while not se_movio:
        se_movio = menu_mover_jugadores(jugadores,cancha)  
    
def opcion_registrar_jugadores(jugadores,cancha):

    for jugador in jugadores:
        posicionar_jugador(jugador, cancha)

    mensaje_ok("Jugadores posicionados correctamente")
            
def jugador_tiene_pelota(jugadores):
    tiene_pelota=-1
    for index,jugador in enumerate(jugadores):
        if jugador["tiene_pelota"]:
            tiene_pelota=index
    return tiene_pelota

def jugador_mas_cercano(index,jugadores):
    jugador_tiene_pelota = jugadores[index]
    distancia_menor = 100
    jugador_cercano = None
    for numero_jugador,jugador in enumerate(jugadores):
        distancia = abs(jugador_tiene_pelota["fila"] - jugador["fila"]) + abs(jugador_tiene_pelota["columna"] - jugador["columna"])
        if distancia < distancia_menor and distancia != 0:
            jugador_cercano = numero_jugador
    return jugadores[jugador_cercano]

def mostrar_jugador_cercano(jugador_pelota,jugador_cercano):
    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print(f"║ Jugador con pelota : {jugador_pelota['nombre']:<24}║")
    print(f"║ Posición: Fila {jugador_pelota['fila']:<3} Columna {jugador_pelota['columna']:<17} ║")
    print("╠══════════════════════════════════════════════╣")
    print(f"║ Jugador mas cercano : {jugador_cercano['nombre']:<23}║")
    print(f"║ Posición: Fila {jugador_cercano['fila']:<3} Columna {jugador_cercano['columna']:<17} ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

def distancia_pelota(jugadores):
        num_jugador=jugador_tiene_pelota(jugadores)
        jugador_cercano=jugador_mas_cercano(num_jugador,jugadores)
        mostrar_jugador_cercano(jugadores[num_jugador],jugador_cercano)


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
        # limpiar_pantalla()

        match opcion:
            case 1:
                opcion_registrar_jugadores(jugadores,cancha)
            case 2:
                mover_jugadores(jugadores,cancha)         
            case 3:
                distancia_pelota(jugadores)
            case 4:
                print("1")
            case 5:
                print("1")
            case _:
                continuar=False
        mostrar_partido(cancha)


def menu(cancha):
    

    limpiar_pantalla()  
    mostrar_partido(cancha)

    controlador_opciones(cancha, JUGADORES)
    
    
    

def mostrar_partido(cancha):
        print("    ", end="")

        for columna in range(COLUMNAS):
            print(f"{columna:<3}", end="")

        print()
        for index,fila in enumerate(cancha):
            print(f"{index:<4}",end="")
            print(f"{"":<2}".join(mostrar_celda(celda) for celda in fila))

def main():

    cancha = generar_cancha()
    
    mostrar_partido(cancha)
    
    menu(cancha)
    
    

if __name__ == "__main__":
    main()