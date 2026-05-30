DISTANCIA_PATADA = 0.35  # Distancia umbral en metros


def calcular_distancia_y_decidir(posicion_robot, posicion_pelota, fase_actual):
    """
    Recibe las posiciones y la fase actual.
    Devuelve la nueva_fase y la distancia calculada.
    """
    # Calcula la diferencia en los ejes X e Y (ignora Z que es la altura)
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]

    # Teorema de Pitágoras para la distancia horizontal
    distancia = (dx**2 + dy**2) ** 0.5

    # Toma de decisión basada en la distancia
    nueva_fase = fase_actual

    # Solo decidimos acercarnos o pararnos si estamos en la fase de búsqueda/aproximación
    if fase_actual in ["inicio", "acercarse"]:
        if distancia > DISTANCIA_PATADA:
            # Si estamos lejos, el robot debe seguir en modo "acercarse"
            nueva_fase = "acercarse"
        else:
            # Si entramos en la zona de pateo, indicamos que es hora de estabilizar
            nueva_fase = "estabilizar"

    return nueva_fase, distancia
