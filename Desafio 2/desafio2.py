def leer_archivo(archivo):
    """
        Args:
        archivo (str): Ruta del archivo a leer.

    Returns:
        str: Cadena de caracteres con el historial de penales en mayúsculas.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato o la cantidad de registros es incorrecta
    
    """
    try:
        with open(archivo, "r") as resultados_grupos:
            historial = resultados_grupos.read().strip().upper()
            if not (1 <= len(historial) <= 1000):
                raise ValueError("La cantidad de registros debe estar en entre 1 a 1000")
        return historial
    
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontro el archivo {archivo}")

def tabla_datos(letras):
    """
    Args:
        letras (str): Cadena de caracteres, cada caracer representa un registro.

    Returns:
        dict: Diccionario final con los registros y sus cantidades correspodientes.

    Raises:
        ValueError: Si el formato no es valido (solo acepta en el registro L, C y R).
    
    """
    
    direcciones={}
        
    for letra in letras:
        if letra == " ":
            continue  # ignora espacios sin cortar el loop
        if letra in {"L", "R", "C"}:
            direcciones[letra] = direcciones.get(letra, 0) + 1
        else: 
            raise ValueError(f"Formato no valido, {letra} no es valido" )        
    return direcciones

def ordenar_prioridad(datos):
    """
    Args:
        datos (dict): Diccionario final con los registros y sus cantidades correspodientes.

    Returns:
        list: Lista ordenada por prioridad siendo de la mas importante a la menos (L -> R -> C).

    """
    datos_finales = datos.items()
    orden = ["C","R","L"]
    lista_datos = sorted(datos_finales,key=lambda direccion: orden.index(direccion[0]))
    return lista_datos


def direccion_dominante(datos):
    """
    Busca el numero mayor y en cazo de empate prioriza la direccion que este mas adelante en la lista.

    Args:
        datos (list): Lista ordenado.

    Returns:
        tupla(str,int): Tupla con el valor de mayor cantidad (registro, cantidad)
    """
    cant_mayor = 0
    for dato in datos:
        if dato[1] >= cant_mayor:
            dirc_dominante = dato[0]
            cant_mayor = dato[1]

    return (dirc_dominante, cant_mayor)


def prediccion_penales(historial):
    """
    Imprime en pantalla el registro con mayor cantidad y prioritario a los demas.
    
    Args:
        historial (str): Cadena de caracteres con el historial de penales.
    """
    
    
    tabla = tabla_datos(historial)
    
    resultado = direccion_dominante(ordenar_prioridad(tabla))
    print(resultado[0])
    print(resultado[1])


def mensaje_salida():
    """
    Solicita al usuario si desea salir del programa.

    Returns:
        bool: False si el usuario desea salir, True si desea continuar.
    """
    respuesta = input("¿Desea salir? (s/n): ")
    return respuesta.lower() == "n"  # True = continuar, False = salir

def main():
    """
    Punto de entrada del programa. Contiene el loop principal que solicita
    la ruta del archivo, procesa el estadisticas de penales de un jugador y 
    mostrar la tendencia de disparo Centro , Izquierda y Derecha.
    
    Permite reintentar ante errores y salir cuando el usuario lo indique.
    """
    continuar = True
    while continuar:
        try:
            ruta_archivo = input("Ingrese el nombre del archivo .txt: ")+".txt"
            prediccion_penales(leer_archivo(ruta_archivo))
            
        except Exception as e:
            print(f"Error: {e}")
        
        continuar = mensaje_salida()
            

if __name__ == "__main__":
    main()