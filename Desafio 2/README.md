# Predicción de Penales — Desafío 2
### Copa de Algoritmia y Programación UADE 2026

---

## Equipo

**ARC**

| Integrante |
|---|
| Agustina Fernandez Haisner |
| Royer Rolando Yampasi Laura |
| Carlos Daniel Lazo Corrales |

---

## Descripción

Sistema que analiza el historial reciente de penales de un jugador rival y predice hacia qué dirección es más probable que patee. Dado un archivo con la secuencia de penales, el programa cuenta las apariciones de cada dirección y determina la dominante, aplicando reglas de desempate táctico en caso de empate.

---

## Requisitos

- Python 3.x
- Sin librerías externas (solo librería estándar)

---

## Uso

1. Ejecutar el programa:
```bash
python desafio2.py
```

2. Ingresar archivo cuando se solicite:

Ingrese el nombre del archivo .txt y programa agrega `.txt` automáticamente.

3. El programa muestra la dirección dominante y su frecuencia, luego pregunta si se desea continuar o salir.

---

## Formato del archivo de entrada

Una sola línea con la secuencia de penales. Cada carácter representa un penal:

| Carácter | Dirección |
|----------|-----------|
| `L`      | Izquierda |
| `R`      | Derecha   |
| `C`      | Centro    |

El programa acepta tanto mayúsculas como minúsculas.

**Restricciones:**
- Longitud entre 1 y 1000 caracteres
- Solo puede contener los caracteres `L`, `R` y `C`

**Ejemplo:**
```
LRRCLRRLLR
```

---

## Formato de salida

```
R
5
```

Primera línea: dirección más frecuente.
Segunda línea: cantidad de apariciones.

---

## Regla de desempate

Si dos o más direcciones tienen la misma frecuencia, se aplica prioridad táctica:

**L > R > C**

Es decir, izquierda tiene prioridad sobre derecha, y derecha sobre centro.

---

## Estructura del código

| Función | Descripción |
|---|---|
| `leer_archivo(archivo)` | Lee el archivo y devuelve el historial como string en mayúsculas |
| `tabla_datos(letras)` | Cuenta las apariciones de cada dirección en un diccionario |
| `ordenar_prioridad(datos)` | Ordena las direcciones según la prioridad táctica (C, R, L) |
| `direccion_dominante(datos)` | Identifica la dirección con mayor frecuencia |
| `prediccion_penales(historial)` | Coordina el procesamiento completo |
| `mensaje_salida()` | Gestiona la opción de continuar o salir del programa |
| `main()` | Punto de entrada, contiene el loop principal |

---

## Manejo de errores

| Situación | Mensaje |
|---|---|
| Archivo no encontrado | `No se encontro el archivo [nombre]` |
| Historial fuera de rango (>1000) | `La cantidad de registros debe estar en entre 1 a 1000` |
| Carácter inválido en la secuencia | `Formato no valido, [caracter] no es valido` |

Ante cualquier error se muestra un mensaje descriptivo y se ofrece intentar con otro archivo.
