# ARC Torneo Python - Sistema de Clasificación FIFA 🏆

## 📝 Descripción
Este proyecto implementa un sistema automatizado para calcular la clasificación de la fase de grupos de la Copa del Mundo FIFA 2026. Procesa los resultados de una serie de partidos y determina qué equipos avanzan a la siguiente fase aplicando las reglas oficiales de puntuación y los criterios de desempate de la FIFA.

## ✨ Características
- **Procesamiento de Partidos:** Lectura automatizada de resultados desde un archivo de texto (`archivo.txt`).
- **Cálculo de Estadísticas:** Cómputo automático de puntos, goles a favor, goles en contra y diferencia de goles.
- **Sistema de Desempate Completo:** Resuelve igualdades de puntos utilizando (en orden de prioridad):
  1. Diferencia de gol.
  2. Mayor cantidad de goles a favor.
  3. Orden alfabético (Corner case: en caso de un empate absoluto).
- **Salida Estandarizada:** Genera el reporte exacto indicando el primer clasificado, el segundo y el tercer puesto.

## 🚀 Uso

### Formato de Entrada
Crea un archivo llamado `archivo.txt` en la misma ruta que el script. La primera línea debe contener el total de partidos, y las siguientes líneas el resultado en el formato `EquipoLocal EquipoVisitante GolesLocal GolesVisitante`.

**Ejemplo (`archivo.txt`):**
```text
6
ARG BRA 2 1
BRA ESP 1 1
ESP ARG 3 0
ARG JPN 2 0
BRA JPN 2 1
ESP JPN 1 0
```

### Ejecución
Para iniciar el procesamiento, ejecuta el script principal en la terminal:
```bash
python desafio1.py
```

### Salida Esperada
```text
Clasificados:
ESP
ARG
Tercero:
BRA
```

## 🛠 Tecnologías Utilizadas
- **Python 3.x**
- Módulo nativo `re` para validaciones por expresiones regulares.