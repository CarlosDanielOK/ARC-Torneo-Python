def detectar_distancia(posicion_pelota, posicion_robot):
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]
    distancia = (dx**2 + dy**2) ** 0.5
    return distancia

def acercarse_pelota(posicion_pelota, posicion_robot):
    DISTANCIA_PATADA = 0.35
    while detectar_distancia(posicion_pelota, posicion_robot) > DISTANCIA_PATADA:
        caminar(velocidad=1.0*detectar_distancia(posicion_pelota, posicion_robot))
    pararse()

def patear_pelota():
    inclinarse(adelante=1.0, izquierda=0.5)
    preparar_patada(pierna='derecha', fuerza=1.0)
    patear(pierna='derecha', potencia=1.0)
    pararse() 

