



def estado_robot(torso):
    """
    Devuelve esl estado del robot
     #Suponemos que estado_torso devuelve una tupla de numeros, y 0 significa que esta todo en su posicion original.

    Args:
        torso : Estado del torso del robot
    """

    ESTADO = True
    if torso[0] != 0 or torso[1] != 0 or torso[2] != 0 or torso[3] != 0:
        ESTADO = False
    return ESTADO

def detectar_distancia(posicion_pelota, posicion_robot):
    """Calcula la distancia entre el Robot y la Pelota

    Args:
        posicion_pelota (x,y,z): Posición de la pelota en el espacio 
        posicion_robot (x,y,z): Posición de la pelota en el espacio

    Returns:
        distancia (Int): Distancia calculada
    """
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]
    distancia = (dx**2 + dy**2) ** 0.5
    return distancia

def acercarse_pelota(posicion_pelota, posicion_robot):
    """Mientras la distancia sea mayor que la DISTANCIA_PATADA elegido, se deberá llamar a caminar(velocidad). 
        - velocidad incrementa segun la distancia entre la pelota y el robot

    Args:
        posicion_pelota (x,y,z): Posición de la pelota en el espacio 
        posicion_robot (x,y,z): Posición de la pelota en el espacio
    """
    DISTANCIA_PATADA = 0.35
    while detectar_distancia(posicion_pelota, posicion_robot) > DISTANCIA_PATADA:
        caminar(velocidad=1.0*detectar_distancia(posicion_pelota, posicion_robot))
    pararse()

def patear_pelota():
    '''
        Prepara al robot para patear a la pelota
        se pestabiliza luego de ejecutar la patada
    '''
    inclinarse(adelante=1.0, izquierda=0.5)
    preparar_patada(pierna='derecha', fuerza=1.0)
    patear(pierna='derecha', potencia=1.0)
    pararse() 


def main():
    """
    cotrola la estabilidad del robot y ejecuta la logica 
    """
    while estado_robot(estado_torso()):
        detectar_distancia(posicion_pelota, posicion_robot)
        acercarse_pelota(posicion_pelota, posicion_robot)
        patear_pelota()
    pararse()
    main()