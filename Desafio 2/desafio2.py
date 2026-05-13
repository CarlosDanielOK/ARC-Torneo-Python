def leer_archivo(archivo):
    try:
        with open(archivo, "r") as resultados_grupos:
            historial=resultados_grupos.read().strip().upper()
            if not (1 <= len(historial) <= 1000):
                raise ValueError("Cantidad de historial eccede las 1000 valores")
        return historial
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontro el archivo {archivo}")

def tabla_datos(letras):
    direcciones={}
        
    for letra in letras:
        if letra == "L" or  letra == "C" or letra == "R":
            direcciones[letra] = direcciones.get(letra, 0) + 1
        else: 
            raise ValueError(f"Formato no valido, {letra} no es valido" )        
    return direcciones

def ordenar_prioridad(datos):
    orden=["C","R","L"]
    lista_datos=sorted(datos,key=lambda direccion: orden.index(direccion[0]))
    return lista_datos


def direccion_dominante(datos):
    cant_mayor = 0
    for dato in datos:
        if dato[1] >= cant_mayor:
            dirc_dominante = dato[0]
            cant_mayor = dato[1]

    return (dirc_dominante, cant_mayor)


def mostrar_resultado(resultado):
    for dato in resultado:
        print(dato)


def prediccion_penales(historial):
    tabla = tabla_datos(historial)
    datos_finales=tabla.items()
    mostrar_resultado(direccion_dominante(ordenar_prioridad(datos_finales)))


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
    la ruta del archivo, procesa el torneo y muestra los resultados.
    Permite reintentar ante errores y salir cuando el usuario lo indique.
    """
    continuar=True
    while continuar:
        try:
            ruta_archivo = input("Ingrese la nombre del archivo .txt: ")+".txt"
            prediccion_penales(leer_archivo(ruta_archivo))
            
        except Exception as e:
            print(f"Error: {e}")
        
        continuar = mensaje_salida()
            

if __name__ == "__main__":
    main()