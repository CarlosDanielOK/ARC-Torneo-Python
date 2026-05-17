def leer_archivo(archivo):
    """
    Lee y procesa el archivo .txt como el historial de penales de un jugador.

    Args:
        archivo (str): Ruta del archivo a leer.

    Returns:
        str: Cadena de caracteres con el historial de penales en mayúsculas.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato o la cantidad de registros es incorrecta
    
    """
    try:
        with open(archivo, "r") as resultados_penales:
            historial = resultados_penales.read().strip().upper()
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


def direccion_dominante(tabla):
    """
    Ordena segun la mayor cantidad y en caso de empate prioriza L > R > C.
    Devuelve la direccion dominante.

    Args:
        tabla(dict[str, int]): Diccionario con las direcciones y su cantidad de apariciones.

    Returns:
        tupla(str,int): Tupla con los valores de la direccion dominante (direccion, cantidad)
    """
    prioridad = {"L": 2,"R": 1,"C": 0}

    return max(tabla.items(), key = lambda x: (x[1], prioridad[x[0]]))


def prediccion_penales(historial):
    """
    Imprime en pantalla el registro con mayor cantidad y prioritario a los demas.
    
    Args:
        historial (str): Cadena de caracteres con el historial de penales.
    """
    tabla = tabla_datos(historial)
    
    resultado = direccion_dominante(tabla)
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
            ruta_archivo = input("Ingrese el nombre del archivo .txt: ").strip()
            if not ruta_archivo.endswith(".txt"):
                ruta_archivo += ".txt"
            prediccion_penales(leer_archivo(ruta_archivo))
            
        except Exception as e:
            print(f"Error: {e}")
        
        continuar = mensaje_salida()
            

if __name__ == "__main__":
    main()