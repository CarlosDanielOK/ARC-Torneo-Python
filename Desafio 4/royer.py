FILAS = 30
COLUMNAS =50
OBJETOS=["R","O"]
import random

def generar_cancha():
    """Crea y devuelve una matriz de FILAS x COLUMNAS inicializada con '.'.
    Returns:
        list: Matriz de FILAS x COLUMNAS con todas las celdas vacías representadas por '.'.
    """
    cancha = []
    for fila in range(FILAS):
        fila_nueva = []
        for columna in range(COLUMNAS):
            fila_nueva.append(".")
        cancha.append(fila_nueva)
    return cancha

def posicionar(objeto,cancha):
    '''
        Genera la posicion del robot dentro de la cancha , posicion aleatoria
        args:
            cancha: Matriz representativa de la cancha 40X60
    '''
    columna = random.randrange(0,COLUMNAS-1)
    fila = random.randrange(0,FILAS-1)
    cancha[fila][columna]=objeto

    return(fila,columna)

def mostrar_celda(celda):
    """Devuelve la representación visual con color ANSI de una celda de la cancha.
    Args:
        celda (str): Contenido de la celda ('X' o '.').
    Returns:
        str: Cadena con código de color ANSI y el carácter de la celda.
    """
    if celda == "R":
        return "\033[92mR\033[0m"   # rojo - obstáculo
    elif celda == "O":
        return "\033[91mO\033[0m"   # rojo - obstáculo
    else:
        return "."
    
def mostrar_cancha(cancha):
    """Muestra la cancha en consola con coordenadas de filas y columnas y colores por celda.
    Args:
        cancha (list): Matriz de FILAS x COLUMNAS que representa el estado del partido.
    """
    print("    ", end="")

    for columna in range(COLUMNAS):
        print(f"{columna:<3}", end="")

    print()
    for index,fila in enumerate(cancha):
        print(f"{index:<4}",end="")
        print("  ".join(mostrar_celda(celda) for celda in fila))

def detectar_distancia(posicion_pelota, posicion_robot):
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]
    distancia = (dx**2 + dy**2) ** 0.5
    return distancia
def pararse():
    return True
def caminar(velocidad):
    if velocidad>30:
        print("")
    elif velocidad>10:
        print("")
    print(velocidad)
    return True
def acercarse_pelota(posicion_pelota, posicion_robot,cancha):
    DISTANCIA_PATADA = 0.35
    caminar(velocidad=1.0*detectar_distancia(posicion_pelota, posicion_robot))
    


def main():
    """Punto de entrada del programa. Genera la cancha vacía e inicia el menú principal."""
    cancha = generar_cancha()
    posicionRobot=posicionar(OBJETOS[0],cancha)
    posicionPelota=posicionar(OBJETOS[1],cancha)
    distancia=detectar_distancia(posicionPelota,posicionRobot)
    mostrar_cancha(cancha)
    acercarse_pelota(posicionPelota,posicionRobot,cancha)
if __name__ == "__main__":
    main()



