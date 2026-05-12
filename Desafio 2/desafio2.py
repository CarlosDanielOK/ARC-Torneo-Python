def leer_archivo(archivo):

        with open(archivo, "r") as resultados_grupos:
            historial=resultados_grupos.read().strip()

        print(historial)
        return historial

def mensaje_salida():
    """
    Solicita al usuario si desea salir del programa.

    Returns:
        bool: True si el usuario desea salir, False si desea continuar.
    """
    respuesta = input("¿Desea salir? (s/n): ")
    if respuesta.lower() != "n":
        print("Saliendo...")
        return True
    return False


def main():
    """
    Punto de entrada del programa. Contiene el loop principal que solicita
    la ruta del archivo, procesa el torneo y muestra los resultados.
    Permite reintentar ante errores y salir cuando el usuario lo indique.
    """
    while True:
        try:
            ruta_archivo = input("Ingrese la nombre del archivo .txt: ")+".txt"
            leer_archivo(ruta_archivo)
        except Exception as e:
            print(f"Error: {e}")
        
        if mensaje_salida():
            break

if __name__ == "__main__":
    main()