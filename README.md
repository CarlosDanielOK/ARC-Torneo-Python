# Sistema de Clasificación FIFA — Desafío 1
### Copa de Algoritmia y Programación UADE 2026

---

## Equipo

**ARC**

| Integrante |
|---|
| Agustina Fernandez Haisner |
| Royer Rolando Yampasi Laura |
| Carlos Daniel Corrales Lazo |

---

## Descripción

Sistema que procesa los resultados de la fase de grupos del Mundial 2026 y determina los equipos clasificados. Dado un archivo con los resultados de los 6 partidos del grupo, el programa construye la tabla de posiciones, aplica los criterios de desempate oficiales de la FIFA y muestra los dos clasificados y el tercer puesto.

---

## Requisitos

- Python 3.x
- Librería estándar: `re` (incluida en Python, no requiere instalación)

---

## Uso

1. Ejecutar el programa:
```bash
python desafio1.py
```

2. Ingresar la ruta del archivo con los resultados cuando se solicite:
```
Ingrese la direccion del archivo: resultados.txt
```

3. El programa muestra los clasificados y pregunta si se desea continuar o salir.

---

## Formato del archivo de entrada

- **Primera línea:** cantidad de partidos (debe ser 6)
- **Siguientes líneas:** un partido por línea con el formato:

```
EquipoLocal EquipoVisitante GolesLocal GolesVisitante
```

**Restricciones del archivo:**
- Exactamente 4 equipos distintos
- Cada equipo juega exactamente 3 partidos
- Los nombres de equipo deben ser 3 letras mayúsculas (ej: `ARG`, `ESP`)
- Los goles deben ser números enteros entre 0 y 20
- El equipo local y visitante no pueden ser el mismo

**Ejemplo:**
```
6
ARG BRA 2 1
BRA ESP 1 1
ESP ARG 3 0
ARG JPN 2 0
BRA JPN 2 1
ESP JPN 1 0
```

---

## Formato de salida

```
Clasificados:
ESP
ARG
Tercero:
BRA
```

---

## Sistema de puntuación y desempate

**Puntos por partido:**
| Resultado | Puntos |
|-----------|--------|
| Victoria  | 3      |
| Empate    | 1      |
| Derrota   | 0      |

**Criterios de desempate (en orden):**
1. Mayor cantidad de puntos
2. Mayor diferencia de gol (goles a favor − goles en contra)
3. Mayor cantidad de goles a favor
4. Orden alfabético (en caso de empate absoluto)

---

## Estructura del código

| Función | Descripción |
|---|---|
| `leer_archivo(archivo)` | Lee y valida el archivo de entrada usando expresiones regulares |
| `resultado(goles_local, goles_visita)` | Determina si ganó el local, el visitante o hubo empate |
| `tabla_de_datos(partidos)` | Inicializa el diccionario de estadísticas por equipo |
| `partidos_jugados(info_equipos, local, visita)` | Suma 1 al contador de partidos de cada equipo |
| `puntos(info_equipos, local, visita, resultado)` | Asigna puntos según el resultado del partido |
| `goles(info_equipos, local, visita, goles_local, goles_visita)` | Actualiza goles a favor y en contra de cada equipo |
| `diferencia_de_goles(info_equipos, equipo)` | Calcula la diferencia de gol de un equipo |
| `clasificacion(info_equipos)` | Ordena los equipos aplicando todos los criterios de desempate |
| `procesar_torneo(partidos)` | Coordina el procesamiento completo del torneo |
| `mostrar_resultados(equipos)` | Imprime la salida en el formato requerido |
| `mensaje_salida()` | Gestiona la opción de continuar o salir del programa |
| `main()` | Punto de entrada, contiene el loop principal |

---

## Manejo de errores

El programa valida y reporta los siguientes errores sin interrumpirse:

| Situación | Mensaje |
|---|---|
| Archivo no encontrado | `El archivo no existe` |
| Primera línea no es un número | `La primera línea debe ser la cantidad de partidos` |
| Cantidad de partidos distinta de 6 | `Se esperaban 6 partidos, el archivo indica N partidos` |
| Formato incorrecto de partido | `Error en datos del archivo, formato de partidos mal ingresados` |
| Menos o más de 4 equipos distintos | `Cantidad de equipos erronea, verificar que sean 4 equipos` |
| Algún equipo con partidos jugados distinto de 3 | `[equipo] tiene una cantidad inválida de partidos` |

Ante cualquier error se muestra un mensaje descriptivo y se ofrece intentar con otro archivo.

---

## Casos de prueba

| # | Descripción | Resultado esperado |
|---|---|---|
| 1 | Ejemplo de la consigna, tabla sin empates | `ESP / ARG / Tercero: BRA` |
| 2 | Desempate por goles a favor (misma DG y pts) | `ESP / BRA / Tercero: ARG` |
| 3 | Desempate alfabético puro (todo igual) | `ARG / BRA / Tercero: ESP` |
| 4 | Todos con 4 puntos, desempate por diferencia de gol | `ARG / BRA / Tercero: ESP` |
| 5 | Goles máximos permitidos (20) | `ARG / BRA / Tercero: JPN` |
| 6 | Todos los partidos 0-0, empate absoluto | `ARG / BRA / Tercero: ESP` |
| 7 | Un equipo gana todos sus partidos | `ARG / ESP / Tercero: BRA` |
| 8 | Primera línea no es número | Error |
| 9 | Primera línea indica 5 partidos | Error |
| 10 | Nombre de equipo en minúsculas | Error |
| 11 | Nombre de equipo con 4 letras | Error |
| 12 | Equipo jugando contra sí mismo | Error |
| 13 | Goles negativos | Error |
| 14 | Goles fuera de rango (21) | Error |
| 15 | Solo 3 equipos distintos | Error |
| 16 | Archivo vacío | Error |
| 17 | Solo la primera línea, sin partidos | Error |
