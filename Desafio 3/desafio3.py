FILAS = 40
COLUMNAS = 60
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]
JUGADORES = [

    # 🔵 Jugador con pelota (Argentina en ataque)
    {"nombre": "DePaul", "equipo": "A", "fila": 20, "columna": 35, "rol": "mediocampista", "tiene_pelota": True},

    # 🟡 Brasil presionando cerca
    {"nombre": "Casemiro", "equipo": "B", "fila": 20, "columna": 33, "rol": "mediocampista", "tiene_pelota": False},
    {"nombre": "Fabinho", "equipo": "B", "fila": 18, "columna": 35, "rol": "mediocampista", "tiene_pelota": False},

    # 🔵 Argentina opciones de pase cortas
    {"nombre": "Messi", "equipo": "A", "fila": 20, "columna": 38, "rol": "delantero", "tiene_pelota": False},
    {"nombre": "Álvarez", "equipo": "A", "fila": 22, "columna": 35, "rol": "delantero", "tiene_pelota": False},

    # 🟡 Brasil cerrando líneas
    {"nombre": "Thiago_Silva", "equipo": "B", "fila": 20, "columna": 30, "rol": "defensor", "tiene_pelota": False},
    {"nombre": "Marquinhos", "equipo": "B", "fila": 22, "columna": 35, "rol": "defensor", "tiene_pelota": False},

    # 🔵 Mediocampo Argentina apoyo
    {"nombre": "Enzo_Fernandez", "equipo": "A", "fila": 18, "columna": 35, "rol": "mediocampista", "tiene_pelota": False},

    # 🟡 Brasil presión alta
    {"nombre": "Vinicius", "equipo": "B", "fila": 25, "columna": 35, "rol": "delantero", "tiene_pelota": False},

    # 🔵 Defensa Argentina
    {"nombre": "Otamendi", "equipo": "A", "fila": 30, "columna": 35, "rol": "defensor", "tiene_pelota": False},
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
    entrada=input(f"\033[96m  ➜  {mensaje}\033[0m ")
    limpiar_pantalla()
    return entrada

def mostrar_cancha(cancha):
        print("    ", end="")

        for columna in range(COLUMNAS):
            print(f"{columna:<3}", end="")

        print()
        for index,fila in enumerate(cancha):
            print(f"{index:<4}",end="")
            print("  ".join(mostrar_celda(celda) for celda in fila))

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
    print("║              0 - Regresar                    ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

def mostrar_jugadores_cercanos(jugador_pelota, jugadores_cercanos):

    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print("║              JUGADORES CERCANOS              ║")
    print("╠══════════════════════════════════════════════╣")
    print(f"║ Jugador con pelota : {jugador_pelota['nombre']:<24}║")
    print(f"║ Posición: Fila {jugador_pelota['fila']:<4} Columna {jugador_pelota['columna']:<17}║")
    print("╠══════════════ Jugadores Cercanos  ═══════════╣")

    for jugador in jugadores_cercanos:
        print(f"║ {jugador['nombre']:<26} F:{jugador['fila']:<6} C:{jugador['columna']:<6} ║")

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
    print("║  0 - Regresar                                                     ║")
    print("╚═══════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

def mostrar_distancia_todos(jugador_pelota, distancia_todos_jugadores):

    print("\033[96m")

    print("╔════════════════ Distancias ══════════════════╗")
    print(f"║ Jugador con pelota : {jugador_pelota['nombre']:<24}║")
    print("╠══════════════════════════════════════════════╣")

    for info in distancia_todos_jugadores:

        jugador = info["jugador"]
        distancia = info["distancia"]

        print(
            f"║ {jugador['nombre']:<18} "
            f" {jugador['equipo']:<3} "
            f"Distancia: {distancia:<10}║"
        )

    print("╚══════════════════════════════════════════════╝")

    print("\033[0m")

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

def mostrar_opciones_registro():
    print("\033[96m")  # cian
    print("╔══════════════════════════════╗")
    print("║     LA CANCHA INTELIGENTE    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Generar jugadores        ║")
    print("║  2. Agregar jugador          ║")
    print("║  0. Regresar                 ║")
    print("╚══════════════════════════════╝")
    print("\033[0m")

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


#### GENERAR CANCHA

def generar_cancha():
    cancha = []
    for fila in range(FILAS):
        fila_nueva = []
        for columna in range(COLUMNAS):
            fila_nueva.append(".")
        cancha.append(fila_nueva)
    return cancha


#### REGISTRAR JUGADORES

def validar_jugador(jugador, jugadores):
    if jugador["rol"] not in ROLES_VALIDOS:
        mensaje_error(f"Rol '{jugador['rol']}' inválido")
        return False
    if jugador["equipo"] not in EQUIPOS_VALIDOS:
        mensaje_error(f"Equipo '{jugador['equipo']}' inválido")
        return False
    if not (0 <= jugador["fila"] < FILAS):
        mensaje_error(f"Fila {jugador['fila']} fuera de la cancha")
        return False
    if not (0 <= jugador["columna"] < COLUMNAS):
        mensaje_error(f"Columna {jugador['columna']} fuera de la cancha")
        return False
    for jugador_posicionado in jugadores:
        if jugador_posicionado['fila'] == jugador["fila"] and jugador_posicionado['columna'] == jugador["columna"]:
            mensaje_error(f"Celda ({jugador['fila']},{jugador['columna']}) ya ocupada")
            return False
        if jugador_posicionado['tiene_pelota'] and jugador["tiene_pelota"]:
            mensaje_error("Ya hay un jugador con la pelota")
            return False
    return True

def posicionar_jugador(jugador,cancha,jugadores_en_cancha):
        cancha[jugador["fila"]][jugador["columna"]]=jugador["equipo"]
        jugadores_en_cancha.append(jugador)

def registrar_jugadores(jugadores,cancha,jugadores_en_cancha):
    for jugador in jugadores:
        valido=validar_jugador(jugador,jugadores_en_cancha)
        if valido:
            posicionar_jugador(jugador, cancha,jugadores_en_cancha)
        else:
            mensaje_error(f"{jugador['nombre']} - No cumple con los parametros")
    mensaje_ok("Jugadores posicionados correctamente")

def agregar_jugador(cancha, jugadores_en_cancha):
    """
    Solicita los datos de un jugador por consola, los valida y lo agrega a la cancha.

    Args:
        cancha (list): Matriz del partido
        jugadores_en_cancha (list): Lista de jugadores ya registrados
    """
    print("\033[96m")
    print("╔══════════════════════════════════════════════╗")
    print("║            AGREGAR JUGADOR                   ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

    # Nombre
    nombre = pedir_input("Nombre del jugador:").strip()
    if not nombre:
        mensaje_error("El nombre no puede estar vacío")
        return

    # Equipo
    print("\033[96m")
    for index, equipo in enumerate(EQUIPOS_VALIDOS):
        equipo_nombre = "Argentina" if equipo == "A" else "Brasil"
        print(f"  {index + 1} - {equipo_nombre}")
    print("\033[0m")
    try:
        opcion_equipo = int(pedir_input("Seleccione equipo:")) - 1
        if not (0 <= opcion_equipo < len(EQUIPOS_VALIDOS)):
            mensaje_error("Equipo inválido")
            return
        equipo = EQUIPOS_VALIDOS[opcion_equipo]
    except ValueError:
        mensaje_error("Ingrese un número válido")
        return

    # Rol
    print("\033[96m")
    for index, rol in enumerate(ROLES_VALIDOS):
        print(f"  {index + 1} - {rol}")
    print("\033[0m")
    try:
        opcion_rol = int(pedir_input("Seleccione rol:")) - 1
        if not (0 <= opcion_rol < len(ROLES_VALIDOS)):
            mensaje_error("Rol inválido")
            return
        rol = ROLES_VALIDOS[opcion_rol]
    except ValueError:
        mensaje_error("Ingrese un número válido")
        return

    # Posición
    try:
        fila    = int(pedir_input(f"Fila (0 a {FILAS - 1}):"))
        columna = int(pedir_input(f"Columna (0 a {COLUMNAS - 1}):"))
    except ValueError:
        mensaje_error("Fila y columna deben ser números")
        return

    # Pelota
    print("\033[96m")
    print("  1 - Sí")
    print("  2 - No")
    print("\033[0m")
    try:
        tiene_pelota = int(pedir_input("¿Tiene la pelota?:")) == 1
    except ValueError:
        mensaje_error("Ingrese un número válido")
        return

    jugador = {
        "nombre":       nombre,
        "equipo":       equipo,
        "fila":         fila,
        "columna":      columna,
        "rol":          rol,
        "tiene_pelota": tiene_pelota
    }

    valido = validar_jugador(jugador, jugadores_en_cancha)
    if valido:
        posicionar_jugador(jugador, cancha,jugadores_en_cancha)
        mensaje_ok(f"{nombre} agregado correctamente en fila {fila}, columna {columna}")
    else:
        mensaje_error(f"{nombre} no pudo agregarse, verificá posición, equipo, rol o pelota")

def generar_partido(cancha,jugadores_en_cancha,jugadores):

    # Menu de opcion de registro de jugadores
    mostrar_opciones_registro()
    try:
        opcion = int(pedir_input("Seleccione una opcion: "))
        match opcion:
            case 1:
                registrar_jugadores(jugadores,cancha,jugadores_en_cancha)
            case 2:
                agregar_jugador(cancha,jugadores_en_cancha)
            case 0 :
                mensaje_info("Regresando...")
            case _:
                mensaje_error("Opcion invalida")
    except ValueError:
        mensaje_error("Ingrese una opcion valida")


#### MOVER JUGADORES 

def elegir_movimientos(jugador):

    movimientos_posibles=["arriba","abajo","izquierda","derecha"]
    movimiento="cancelar"
    mostrar_menu_movimientos(jugador)

    try:
        opcion = int(pedir_input("Seleccione una opcion: "))
        if 1 <= opcion <= 4:
            movimiento = movimientos_posibles[opcion - 1]

        elif opcion == 0:
            movimiento = "cancelar"

        else:
            mensaje_error("Opción inválida")
    except ValueError:
        mensaje_error("Ingrese un número válido")
        
    return movimiento    

def ejecutar_movimiento(jugador,cancha):
    """Realiza el movimiento del jugador en la cnacha en 4 direcciones (arriba, abajo, derecha, izquierda)

    Args:
        jugador {dict}: Informacion del jugador que realizara el movimiento en la cancha 
        cancha List[List]: Matriz de 40x60 que representa la cancha 

    Raises:
        IndexError: _description_
        IndexError: _description_
        IndexError: _description_
        IndexError: _description_
        print: _description_

    Returns:
        bool: True si se realizo el movimiento del jugador dentro de la cancha
    """
    fila=jugador["fila"]
    columna=jugador["columna"]

    movimiento=elegir_movimientos(jugador)

    se_movio=False
    match movimiento:
        case "arriba":
            arriba=fila-1
            if arriba >= 0 and cancha[arriba][columna] == '.':
                cancha[arriba][columna] = jugador["equipo"]  # ← modifica la matriz
                jugador["fila"] = arriba
                mensaje_ok(f"{jugador['nombre']} se movió ⬆ arriba")
                se_movio = True
            else:
                mensaje_error("Movimiento inválido: posición fuera de límites o celda ocupada")
                se_movio = False

        case "abajo":
            abajo=fila+1
            if abajo< FILAS and cancha[abajo][columna]=='.':
                cancha[abajo][columna]=jugador["equipo"]
                jugador["fila"]=abajo
                mensaje_ok(f"{jugador['nombre']} se movió ⬇ abajo")
                se_movio=True
            else:
                mensaje_error("Movimiento inválido: posición fuera de límites o celda ocupada")
                se_movio = False
        case "izquierda":
            izquierda=columna-1
            if izquierda >= 0 and cancha[fila][izquierda]=='.':
                mensaje_ok(f"{jugador['nombre']} se movió ⬅ izquierda")
                cancha[fila][izquierda]=jugador["equipo"]
                jugador["columna"]=izquierda
                se_movio=True
            else:
                mensaje_error("Movimiento inválido: posición fuera de límites o celda ocupada")
                se_movio = False
        case "derecha":
            derecha=columna+1
            if derecha< COLUMNAS and cancha[fila][derecha]=='.':
                cancha[fila][derecha]=jugador["equipo"]
                jugador["columna"]=derecha
                mensaje_ok(f"{jugador['nombre']} se movió ➡ derecha")
                se_movio=True
            else:
                mensaje_error("Movimiento inválido: posición fuera de límites o celda ocupada")
                se_movio = False
        case _:
            mensaje_advertencia("Movimiento cancelado")
            se_movio = False
    if se_movio:
        cancha[fila][columna]="."

    return se_movio

def seleccionar_jugador_para_mover(jugadores, cancha):

    resultado = False
    mostrar_cancha(cancha)
    mostrar_lista_jugadores(jugadores)

    try:
        jugador_index = int(pedir_input("Seleccione un jugador para mover: ")) - 1

        if jugador_index == -1:

            resultado = "salir"

        elif 0 <= jugador_index < len(jugadores):

            jugador_seleccionado = jugadores[jugador_index]

            resultado = ejecutar_movimiento(jugador_seleccionado, cancha)

        else:
            mensaje_error("Jugador fuera de rango")

    except ValueError:
        mensaje_error("Ingrese un número válido")

    return resultado

def mover_jugadores(jugadores, cancha):

    continuar = True

    while continuar:

        resultado = seleccionar_jugador_para_mover(jugadores, cancha)

        if resultado == "salir":
            continuar = False

        elif resultado:
            mensaje_ok("Movimiento realizado")

        else:
            mensaje_error("No se pudo realizar el movimiento")        

#### Distancia de jugadores
def jugador_mas_cercano(indice_con_pelota,jugadores,distancia_todos_jugadores):
    jugador_con_pelota = jugadores[indice_con_pelota]
    distancia_menor = FILAS+COLUMNAS
    jugadores_cercanos=[]
    for jugador in jugadores:
        distancia = abs(jugador_con_pelota["fila"] - jugador["fila"]) + abs(jugador_con_pelota["columna"] - jugador["columna"])
        if distancia != 0:
            distancia_todos_jugadores.append({
                "jugador": jugador,
                "distancia": distancia
            })
            if distancia < distancia_menor and jugador["equipo"] == jugador_con_pelota["equipo"]:
                distancia_menor = distancia
                jugadores_cercanos = [jugador]
            elif distancia == distancia_menor:
                jugadores_cercanos.append(jugador)
    return jugadores_cercanos

def distancia_pelota(jugadores):
    """
    Args:
        Jugadores [dict]: Lista de jugadores, [jugador{nombre,fila,columna,equipo,rol,tiene_pelota}]
    """
    indice_jugador=indice_jugador_con_pelota(jugadores)
    distancia_todos_jugadores=[]
    if indice_jugador >= 0:
        jugadores_cercanos=jugador_mas_cercano(indice_jugador,jugadores,distancia_todos_jugadores)
        mostrar_distancia_todos(
            jugadores[indice_jugador],
            distancia_todos_jugadores
        )
        mostrar_jugadores_cercanos(
            jugadores[indice_jugador],
            jugadores_cercanos)
        pedir_input("Enter para continuar...")
    else:
        mensaje_error("Nadie tiene el balón")

#### DETECTAR PASES

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

def menu_pases(jugador_con_pelota, posibles_pases, jugadores):
    print("\033[96m")
    print("╔═══════════════ Posibles pases ═══════════════╗")
    print(f"║ Jugador con pelota : {jugador_con_pelota['nombre']:<24}║")
    print(f"║ Posición: Fila {jugador_con_pelota['fila']:<3} Columna {jugador_con_pelota['columna']:<17} ║")
    print("╠════════════════ OPCIONES ════════════════════╣")

    mapa_opciones = {}
    contador = 1

    # izquierda
    if posibles_pases["izq"]:
        for jugador in posibles_pases["izq"]:
            if jugador["equipo"] == jugador_con_pelota["equipo"]:
                print(f"║ {contador} - {jugador['nombre']} (izq){"":<28} ║")
                mapa_opciones[contador] = jugador
                contador += 1

    # derecha
    if posibles_pases["der"]:
        for jugador in posibles_pases["der"]:
            if jugador["equipo"] == jugador_con_pelota["equipo"]:
                print(f"║ {contador} - {jugador['nombre']} (der){"":<29} ║")
                mapa_opciones[contador] = jugador
                contador += 1

    # arriba
    if posibles_pases["arr"]:
        for jugador in posibles_pases["arr"]:
            if jugador["equipo"] == jugador_con_pelota["equipo"]:
                print(f"║ {contador} - {jugador['nombre']} (arr){"":<29} ║")
                mapa_opciones[contador] = jugador
                contador += 1

    # abajo
    if posibles_pases["ab"]:
        for jugador in posibles_pases["ab"]:
            if jugador["equipo"] == jugador_con_pelota["equipo"]:
                print(f"║ {contador} - {jugador['nombre']} (ab){"":<28} ║")
                mapa_opciones[contador] = jugador
                contador += 1
            else:
                break
    print(f"║ 0 - Cancelar{"":<32} ║")
    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

    if not mapa_opciones:
        mensaje_advertencia("No hay pases disponibles")
        return

    try:
        opcion = int(pedir_input("Elegir pase: "))

        if opcion == 0:
            return

        if opcion not in mapa_opciones:
            mensaje_error("Opción inválida")
            return

        jugador_destino = mapa_opciones[opcion]

        # 🔁 ejecutar pase directo
        jugador_con_pelota["tiene_pelota"] = False
        jugador_destino["tiene_pelota"] = True

        mensaje_ok(f"Pase realizado a {jugador_destino['nombre']}")

    except ValueError:
        mensaje_error("Entrada inválida")

def detectar_pases(jugadores,cancha):
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
        pasar_a_jugador=-1
        for indice,jugador in enumerate(jugadores):
            if not jugador is jugador_con_pelota:
                clasificar_jugador_por_direccion(jugador,jugador_con_pelota,posibles_pases)        
        mostrar_cancha(cancha)
        menu_pases(jugador_con_pelota, posibles_pases, jugadores)
    else:
        mensaje_error("Ningun jugador tiene la pelota")


#### CAMINO LIBRE AL ARCO

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
    Recorre todos los delanteros y detecta cuáles tienen camino libre al arco rival.

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
        nombre       = jugador["nombre"]
        equipo       = jugador["equipo"]
        columna      = jugador["columna"]
        equipo_nombre = "ARG" if equipo == "A" else "BRA"

        if camino_libre_al_arco(jugador, cancha):
            print(f"║ ✅ {nombre:<20} {equipo_nombre} col {columna:<3} LIBRE    ║")
        else:
            print(f"║ ❌ {nombre:<20} {equipo_nombre} col {columna:<3} BLOQUEADO║")

    if not hay_delanteros:
        print("║  No hay delanteros registrados               ║")

    print("╚══════════════════════════════════════════════╝")
    print("\033[0m")

#### MENU DE OPCIONES

def controlador_opciones(cancha,jugadores_en_cancha,jugadores):

    continuar = True

    while continuar:


        opcion_valida = False

        while not opcion_valida:
            mostrar_menu()

            try:
                opcion = int(pedir_input("Seleccione una opcion: "))

                if 0 <= opcion <= 5:
                    opcion_valida = True
                else:
                    mensaje_error("Opción fuera de rango")

            except ValueError:
                mensaje_error("Ingrese un número válido")

        limpiar_pantalla()

        match opcion:
            case 1:
                generar_partido(cancha,jugadores_en_cancha,jugadores)

            case 2:
                mover_jugadores(jugadores_en_cancha,cancha)

            case 3:
                distancia_pelota(jugadores_en_cancha)

            case 4:
                detectar_pases(jugadores_en_cancha,cancha)

            case 5:
                detectar_camino_libre(jugadores_en_cancha, cancha)

            case 0:
                continuar = False

        mostrar_cancha(cancha)

def menu(cancha,jugadores_en_cancha):
    
    limpiar_pantalla()  
    mostrar_cancha(cancha)
    controlador_opciones(cancha,jugadores_en_cancha, JUGADORES)

#### MAIN

def main():

    cancha = generar_cancha()
    jugadores_en_cancha=[]
    menu(cancha,jugadores_en_cancha)

if __name__ == "__main__":
    main()