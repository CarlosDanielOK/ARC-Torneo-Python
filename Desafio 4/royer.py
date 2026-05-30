FILA = 40
COLUMNA =60
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

def posicionarRobot(cancha):
    '''
        Genera la posicion del robot dentro de la cancha , posicion aleatoria
        args:
            cancha: Matriz representativa de la cancha 40X60
    '''
    columna = random.randrange(0,60)
    fila = random.randrange(0,40)
    cancha[fila][columna]="R"

def mostrar_celda(celda):
    """Devuelve la representación visual con color ANSI de una celda de la cancha.
    Args:
        celda (str): Contenido de la celda ('A', 'B', 'X' o '.').
    Returns:
        str: Cadena con código de color ANSI y el carácter de la celda.
    """
    if celda == "A":
        return "\033[94mA\033[0m"   # azul - Argentina
    elif celda == "B":
        return "\033[93mB\033[0m"   # amarillo - Brasil  
    elif celda == "X":
        return "\033[91mX\033[0m"   # rojo - obstáculo
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

def main():
    """Punto de entrada del programa. Genera la cancha vacía e inicia el menú principal."""
    cancha = generar_cancha()
    mostrar_cancha()

if __name__ == "__main__":
    main()