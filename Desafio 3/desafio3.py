FILAS = 40
COLUMNAS = 60
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]
JUGADORES = [
    # Jugador con pelota
    {"nombre": "Pelota",    "equipo": "A", "fila": 10, "columna": 20, "rol": "mediocampista", "tiene_pelota": True},
    
    # Misma fila, distintas columnas
    {"nombre": "CompA_Izq", "equipo": "A", "fila": 10, "columna": 15, "rol": "delantero",      "tiene_pelota": False},  # izq, libre
    {"nombre": "RivalIzq",  "equipo": "B", "fila": 10, "columna": 12, "rol": "defensor",       "tiene_pelota": False},  # izq, rival bloqueador
    {"nombre": "CompA_Izq2","equipo": "A", "fila": 10, "columna": 8,  "rol": "defensor",       "tiene_pelota": False},  # izq, detrás del rival
    {"nombre": "CompA_Der", "equipo": "A", "fila": 10, "columna": 25, "rol": "delantero",      "tiene_pelota": False},  # der, libre
    {"nombre": "RivalDer",  "equipo": "B", "fila": 10, "columna": 30, "rol": "defensor",       "tiene_pelota": False},  # der, rival bloqueador
    {"nombre": "CompA_Der2","equipo": "A", "fila": 10, "columna": 35, "rol": "mediocampista",  "tiene_pelota": False},  # der, detrás del rival

    # Misma columna, distintas filas
    {"nombre": "CompA_Arr", "equipo": "A", "fila": 5,  "columna": 20, "rol": "defensor",       "tiene_pelota": False},  # arriba, libre
    {"nombre": "RivalArr",  "equipo": "B", "fila": 3,  "columna": 20, "rol": "mediocampista",  "tiene_pelota": False},  # arriba, rival bloqueador
    {"nombre": "CompA_Aba", "equipo": "A", "fila": 15, "columna": 20, "rol": "defensor",       "tiene_pelota": False},  # abajo, libre
    {"nombre": "RivalAba",  "equipo": "B", "fila": 18, "columna": 20, "rol": "delantero",      "tiene_pelota": False},  # abajo, rival bloqueador

    # Jugadores que NO deben aparecer (diagonal)
    {"nombre": "Diagonal",  "equipo": "A", "fila": 15, "columna": 25, "rol": "delantero",      "tiene_pelota": False},  # diagonal, ignorar
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

def mostrar_lista_jugadores(jugadores):
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

def mostrar_cancha(cancha):
        print("    ", end="")

        for columna in range(COLUMNAS):
            print(f"{columna:<3}", end="")

        print()
        for index,fila in enumerate(cancha):
            print(f"{index:<4}",end="")
            print(f"{"":<2}".join(mostrar_celda(celda) for celda in fila))

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

def mostrar_lista_posibles_pases(jugador,posibles_pases):
    print("\033[96m")
    print("╔═══════════════ Posibles pases ═══════════════╗")
    print(f"║ Jugador con pelota : {jugador['nombre']:<24}║")
    print(f"║ Posición: Fila {jugador['fila']:<3} Columna {jugador['columna']:<17} ║")
    print("╠════════════════ Columna izq  ════════════════╣")
    if posibles_pases["izq"]:
        for jugador_fila in posibles_pases["izq"]:
            if jugador["equipo"]!=jugador_fila["equipo"]:
                break
            print(f"║ Jugador mas cercano : {jugador_fila['nombre']:<23}║")
            print(f"║ Posición: Fila {jugador_fila['fila']:<3} Columna {jugador_fila['columna']:<17} ║")
    print("╠════════════════ Columna der  ════════════════╣")
    if posibles_pases["der"]:
        for jugador_fila in posibles_pases["der"]:
            if jugador["equipo"]!=jugador_fila["equipo"]:
                break
            print(f"║ Jugador mas cercano : {jugador_fila['nombre']:<23}║")
            print(f"║ Posición: Fila {jugador_fila['fila']:<3} Columna {jugador_fila['columna']:<17} ║")
    print("╠══════════════════  Fila    ══════════════════╣")
    if posibles_pases["arr"]:
        for jugador_columna in posibles_pases["arr"]:
            if jugador["equipo"]!=jugador_columna["equipo"]:
                break
            print(f"║ Jugador mas cercano : {jugador_columna['nombre']:<23}║")
            print(f"║ Posición: Fila {jugador_columna['fila']:<3} Columna {jugador_columna['columna']:<17} ║")
    print("╠══════════════════  Fila    ══════════════════╣")
    if posibles_pases["ab"]:
        for jugador_columna in posibles_pases["ab"]:
            if jugador["equipo"]!=jugador_columna["equipo"]:
                break
            print(f"║ Jugador mas cercano : {jugador_columna['nombre']:<23}║")
            print(f"║ Posición: Fila {jugador_columna['fila']:<3} Columna {jugador_columna['columna']:<17} ║")
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

def ejecutar_movimiento(jugador,cancha):

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
    
def seleccionar_jugador_para_mover(jugadores,cancha):

    se_movio = False
    
    mostrar_lista_jugadores(jugadores)

    jugador_index=int(pedir_input("Seleccione un jugador para mover: "))-1
    
    if jugador_index < 0:
            se_movio=True
    else:
        try:
            jugador_seleccionado=jugadores[jugador_index]
            se_movio = ejecutar_movimiento(jugador_seleccionado,cancha)
        except Exception as e:
                mensaje_error("Opxion invalida")
        
    return se_movio

def mover_jugadores(jugadores,cancha):
    se_movio=False
    while not se_movio:
        se_movio = seleccionar_jugador_para_mover(jugadores,cancha)  

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
        if jugador_posicionado['tiene_pelota'] and jugador["tiene_pelota"]:
            valido=False   
    return valido    

def registrar_jugador(jugador,jugadores):
    
    valido=validar_jugador(jugador,jugadores)
    if valido:
        jugadores.append(jugador)

    return valido    
def registrar_jugadores(jugadores,cancha):

    for jugador in jugadores:
        posicionar_jugador(jugador, cancha)

    mensaje_ok("Jugadores posicionados correctamente")
            
def indice_jugador_con_pelota(jugadores):
    """
    Devuelve el indice del jugador con pelota, tiene_pelota=True

    Args:
        Jugadores [dict]: Lista de jugadores, [jugador{nombre,fila,columna,equipo,rol,tiene_pelota}]
    Returns:
        Int: Indice del jugador con pelota 
    """
    tiene_pelota=-1
    for index,jugador in enumerate(jugadores):
        if jugador["tiene_pelota"]:
            tiene_pelota=index
    return tiene_pelota

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


def jugador_mas_cercano(indice_con_pelota,jugadores):
    jugador_con_pelota = jugadores[indice_con_pelota]
    # jugador_cercanos=[]
    distancia_menor = FILAS+COLUMNAS
    jugador_cercano = None
    for numero_jugador,jugador in enumerate(jugadores):
        distancia = abs(jugador_con_pelota["fila"] - jugador["fila"]) + abs(jugador_con_pelota["columna"] - jugador["columna"])
        if distancia < distancia_menor and distancia != 0:
            jugador_cercano = numero_jugador
            distancia_menor=distancia
    
    return jugadores[jugador_cercano]



def distancia_pelota(jugadores):
    """
    Args:
        jugadores (_type_): _description_
    """
    indice_jugador=indice_jugador_con_pelota(jugadores)
    if indice_jugador >= 0:
        jugador_cercano=jugador_mas_cercano(indice_jugador,jugadores)
        mostrar_jugador_cercano(jugadores[indice_jugador],jugador_cercano)
    else:
        mensaje_error("Nadie tiene el balón")


def insertar_menor_distancia(jugador,distancia_jugador,distancia_actual,posibles_pases):
    '''
    Inserta el jugador al inicio o al final de la la lista de pases posibles , al inicio si la distancia es la menor y si no al final
    '''
    if distancia_jugador < distancia_actual:
        posibles_pases.insert(0,jugador)
    else:
        posibles_pases.append(jugador)

def clasificar_jugador_por_direccion(jugador, jugador_con_pelota,posibles_pases):
    """
        Varifica la direccion en la que apunta el jugador con pelota al jugador que sera el posible pase, (arriba, abajo, izquierda y derecha)
    Args:
        jugador_con_pelota (dict): informacion de jugador{nombre,fila,columna,equipo,rol,tiene_pelota} con pelota
        jugador dict: informacion de jugador{nombre,fila,columna,equipo,rol,tiene_pelota} a comparar distancia
        posibles_pases_fila_izq (List): Lista de posibles pases en la misma fila , a la izquierda del jugador
        posibles_pases_fila_der (List): Lista de posibles pases en la misma fila , a la derecha del jugador
        posibles_pases_columna_arriba (List): Lista de posibles pases en la misma columna , a arriba del jugador
        posibles_pases_columna_abajo (List): Lista de posibles pases en la misma columna , a la abajo del jugador
    """
    misma_fila    = jugador_con_pelota["fila"]    == jugador["fila"]
    misma_columna = jugador_con_pelota["columna"] == jugador["columna"]

    if misma_fila: 
        diferencia_columna = jugador_con_pelota["columna"] - jugador["columna"]
        if diferencia_columna > 0:  #IZQUIERDA
            if not posibles_pases["izq"]:
                posibles_pases["izq"].append(jugador)
            else:
                distancia_jugador = abs(diferencia_columna)
                distancia_actual  = abs(jugador_con_pelota["columna"] - posibles_pases["izq"][0]["columna"]) 
                insertar_menor_distancia(jugador, distancia_jugador, distancia_actual, posibles_pases["izq"])
        elif diferencia_columna < 0:  #DERECHA
            if not posibles_pases["der"]:
                posibles_pases["der"].append(jugador)
            else:
                distancia_jugador = abs(diferencia_columna)
                distancia_actual  = abs(jugador_con_pelota["columna"] - posibles_pases["der"][0]["columna"]) 
                insertar_menor_distancia(jugador, distancia_jugador, distancia_actual, posibles_pases["der"])

    elif misma_columna:
        diferencia_fila = jugador_con_pelota["fila"] - jugador["fila"]
        if diferencia_fila > 0:  #ARRIBA
            if not posibles_pases["arr"]:
                posibles_pases["arr"].append(jugador)
            else:
                distancia_jugador = abs(diferencia_fila)
                distancia_actual  = abs(jugador_con_pelota["fila"] - posibles_pases["arr"][0]["fila"])
                insertar_menor_distancia(jugador, distancia_jugador, distancia_actual, posibles_pases["arr"])
        elif diferencia_fila < 0:  #ABAJO
            if not posibles_pases["ab"]:
                posibles_pases["ab"].append(jugador)
            else:
                distancia_jugador = abs(diferencia_fila)
                distancia_actual  = abs(jugador_con_pelota["fila"] - posibles_pases["ab"][0]["fila"]) 
                insertar_menor_distancia(jugador, distancia_jugador, distancia_actual, posibles_pases["ab"])
            
def detectar_pases(jugadores):
    """
        Verifica los posibles pases en 4 direcciones distintas(arriba, abajo, izquierda y derecha)
    Args:
        jugadores [dict]: Lista de [jugador{nombre,fila,columna,equipo,rol,tiene_pelota}]
    """
    indice=indice_jugador_con_pelota(jugadores) #Int
    if indice >= 0:
        jugador_con_pelota=jugadores[indice] #jugador{}

        posibles_pases={
            "izq":[],
            "der":[],
            "arr":[],
            "ab":[]
        }
        for jugador in jugadores:
            if not jugador is jugador_con_pelota:
                clasificar_jugador_por_direccion(jugador,jugador_con_pelota,posibles_pases)        
        
        mostrar_lista_posibles_pases(jugador_con_pelota,posibles_pases)
        pedir_input("Seleccionar jugador para pasar pelota")
    else:
        mensaje_error("Ningun jugador tiene la pelota")

def camino_libre_al_arco(jugador, cancha):
    """
    Verifica si un delantero tiene camino libre al arco rival en su misma fila.

    Args:
        jugador (dict): Jugador a verificar {nombre, fila, columna, equipo, rol, tiene_pelota}
        cancha (list): Matriz de 40x60 con el estado actual del partido

    Returns:
        bool: True si tiene camino libre, False si no
    """
    if jugador["rol"] != "delantero":
        return False

    equipo  = jugador["equipo"]
    fila    = jugador["fila"]
    columna = jugador["columna"]

    if equipo == "A":
        if columna < 30:
            return False
        rival = "B"
        celdas = range(columna + 1, COLUMNAS)
    else:
        if columna > 29:
            return False
        rival = "A"
        celdas = range(columna - 1, -1, -1)

    for col in celdas:
        celda = cancha[fila][col]
        if celda == rival or celda == "X":
            return False

    return True


def detectar_camino_libre(jugadores, cancha):
    """
    Recorre todos los jugadores y detecta cuáles tienen camino libre al arco rival.

    Args:
        jugadores (list): Lista de jugadores [{nombre, fila, columna, equipo, rol, tiene_pelota}]
        cancha (list): Matriz de 40x60 con el estado actual del partido
    """
    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print("║         CAMINO LIBRE AL ARCO                 ║")
    print("║              Delanteros                      ║")
    print("╠══════════════════════════════════════════════╣")

    hay_delanteros = False

    for jugador in jugadores:
        if jugador["rol"] != "delantero":
            continue

        hay_delanteros = True
        nombre  = jugador["nombre"]
        equipo  = jugador["equipo"]
        columna = jugador["columna"]

        if camino_libre_al_arco(jugador, cancha):
            print(f"║ ✅ {nombre:<20} ({equipo}) col {columna:<3} LIBRE    ║")
        else:
            print(f"║ ❌ {nombre:<20} ({equipo}) col {columna:<3} BLOQUEADO║")

    if not hay_delanteros:
        print("║  No hay delanteros registrados               ║")

    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

def controlador_opciones(cancha,jugadores):

    continuar=True
    while continuar:
        mostrar_menu()

        opcion=int(pedir_input("Seleccione una opcion: "))
        limpiar_pantalla()

        match opcion:
            case 1:
                registrar_jugadores(jugadores,cancha)
            case 2:
                mover_jugadores(jugadores,cancha)         
            case 3:
                distancia_pelota(jugadores)
            case 4:
                detectar_pases(jugadores)
            case 5:
                detectar_camino_libre(jugadores, cancha)
            case _:
                continuar=False
        mostrar_cancha(cancha)


def menu(cancha):
    

    limpiar_pantalla()  
    mostrar_cancha(cancha)

    controlador_opciones(cancha, JUGADORES)

def main():

    cancha = generar_cancha()
    
    mostrar_cancha(cancha)
    
    menu(cancha)
    
    

if __name__ == "__main__":
    main()