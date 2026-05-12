def leer_archivo(archivo):

        with open(archivo, "r") as resultados_grupos:
            historial=resultados_grupos.read().strip()
            if not (1 <= len(historial) <= 1000):
                raise ValueError("Cantidad de historial eccede las 1000 valores")
        return historial


def tabla_datos(letras):
    direcciones={}
        
    for letra in letras:
        letra_Upper=letra.upper()
        if letra_Upper == "L" or  letra_Upper == "C" or letra_Upper == "R":
            direcciones[letra_Upper] = direcciones.get(letra_Upper, 0) + 1
        else: 
            raise ValueError(f"Formato no valido, {letra_Upper} no es valido" )        
    return direcciones


def direccion_dominante(tabla):
    cant_mayor = 0
    for direccion in tabla:
        if tabla[direccion] > cant_mayor:
            dirc_dominante = direccion
            cant_mayor = tabla[direccion]

    return (dirc_dominante, cant_mayor)


def mostrar_resultado(resultado):
    for dato in resultado:
        print(dato)


def prediccion_penales(historial):
    tabla = tabla_datos(historial)
    mostrar_resultado(direccion_dominante(tabla))


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
            prediccion_penales(leer_archivo(ruta_archivo))
            
        except Exception as e:
            print(f"Error: {e}")
        
        if mensaje_salida():
            break

if __name__ == "__main__":
    main()