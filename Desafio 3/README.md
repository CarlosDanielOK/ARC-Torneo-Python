# La Cancha Inteligente — Desafío 3
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

Sistema que simula el posicionamiento y desplazamiento de jugadores en una cancha de fútbol representada como una matriz. El programa permite registrar jugadores, moverlos dentro de la cancha, calcular distancias a la pelota, detectar pases posibles entre compañeros y determinar si un delantero tiene camino libre al arco rival.

---

## Requisitos

- Python 3.10 o superior (se utiliza `match/case`)
- Sin librerías externas (solo librería estándar)

---

## Uso

1. Ejecutar el programa:
```bash
python desafio3.py
```

2. Al iniciarse, se muestra la cancha vacía y el menú principal con las opciones disponibles.

3. Navegar por el menú para registrar jugadores, moverlos y analizar situaciones tácticas.

---

## Representación de la cancha

La cancha es una matriz de **40 filas × 60 columnas** (índices 0–39 y 0–59).

| Símbolo | Significado |
|---------|-------------|
| `.`     | Posición vacía |
| `A`     | Jugador de Argentina |
| `B`     | Jugador de Brasil |
| `X`     | Obstáculo o zona bloqueada |

La pelota no ocupa celda propia: siempre comparte posición con el jugador que la posee.

**Ubicación de los arcos:**
- Arco de Argentina → columna `0`
- Arco de Brasil → columna `59`
- Argentina ataca hacia la derecha; Brasil ataca hacia la izquierda.

---

## Representación de los jugadores

Cada jugador se representa mediante un diccionario con los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| `nombre` | Nombre del jugador |
| `equipo` | `"A"` para Argentina, `"B"` para Brasil |
| `fila` | Fila actual en la cancha (0–39) |
| `columna` | Columna actual en la cancha (0–59) |
| `rol` | `arquero`, `defensor`, `mediocampista` o `delantero` |
| `tiene_pelota` | `True` si el jugador posee la pelota, `False` si no |

---

## Menú principal

```
╔══════════════════════════════╗
║     LA CANCHA INTELIGENTE    ║
╠══════════════════════════════╣
║  1. Registrar jugadores      ║
║  2. Mover jugador            ║
║  3. Distancia a la pelota    ║
║  4. Detectar pases           ║
║  5. Camino libre al arco     ║
║  0. Salir                    ║
╚══════════════════════════════╝
```

---

## Funcionalidades

### Tarea 1 — Crear la cancha
Genera la matriz de 40 × 60 inicializada con `"."` y la retorna.

### Tarea 2 — Registrar jugadores
Permite cargar jugadores de dos formas: generando el conjunto de jugadores predefinido en `JUGADORES`, o agregando un jugador manualmente ingresando sus datos por consola.

En ambos casos se valida que:
- la posición esté dentro de los límites de la cancha;
- la celda destino esté libre;
- el rol sea válido;
- el equipo sea válido;
- solo un jugador tenga la pelota al mismo tiempo.

### Tarea 3 — Mover jugadores
Permite seleccionar un jugador de la lista y desplazarlo una celda en cualquiera de las cuatro direcciones (arriba, abajo, izquierda, derecha). El movimiento se rechaza si la celda destino está fuera de los límites, ocupada por otro jugador o es un obstáculo `"X"`. La matriz se actualiza automáticamente.

### Tarea 4 — Distancia a la pelota
Calcula la **distancia Manhattan** entre el jugador que posee la pelota y todos los demás jugadores. Muestra la distancia de cada uno e indica cuál o cuáles son los más cercanos. En caso de empate, se muestran todos los jugadores empatados.

> Distancia Manhattan = |Δfila| + |Δcolumna|

### Tarea 5 — Detectar pases posibles
Analiza las cuatro direcciones (izquierda, derecha, arriba, abajo) desde el jugador con la pelota y detecta posibles receptores. Un pase es válido únicamente si:
- ambos jugadores pertenecen al mismo equipo;
- están en la misma fila o en la misma columna;
- no hay jugadores rivales ni obstáculos `"X"` en el trayecto.

Los jugadores del mismo equipo no bloquean el pase. No se permiten pases diagonales. Desde el menú de pases se puede ejecutar el pase seleccionado, transfiriendo la posesión de la pelota.

### Tarea 6 — Camino libre al arco
Determina si un delantero tiene camino libre al arco rival en su misma fila. Las condiciones son:
- rol `delantero`;
- ubicado en la **mitad ofensiva** (Argentina: columnas 30–59 / Brasil: columnas 0–29);
- ningún rival ni obstáculo `"X"` entre el jugador y el arco rival en la misma fila.

Los jugadores del mismo equipo no bloquean el camino al arco.

---

## Estructura del código

| Función | Descripción |
|---|---|
| `generar_cancha()` | Crea y retorna la matriz 40×60 inicializada con `"."` |
| `validar_jugador(jugador, jugadores)` | Valida posición, rol, equipo y posesión de pelota |
| `posicionar_jugador(jugador, cancha, jugadores_en_cancha)` | Ubica al jugador en la matriz y lo agrega a la lista |
| `registrar_jugadores(jugadores, cancha, jugadores_en_cancha)` | Carga el conjunto de jugadores predefinido |
| `agregar_jugador(cancha, jugadores_en_cancha)` | Solicita datos por consola y agrega un jugador manualmente |
| `generar_partido(cancha, jugadores_en_cancha, jugadores)` | Submenú para elegir modo de registro |
| `ejecutar_movimiento(jugador, cancha)` | Valida y realiza el movimiento de un jugador; retorna `True`/`False` |
| `seleccionar_jugador_para_mover(jugadores, cancha)` | Permite elegir qué jugador mover de la lista |
| `mover_jugadores(jugadores, cancha)` | Loop principal de movimiento |
| `indice_jugador_con_pelota(jugadores)` | Retorna el índice del jugador que posee la pelota |
| `jugador_mas_cercano(indice, jugadores, distancias)` | Calcula distancias y retorna los jugadores más cercanos |
| `distancia_pelota(jugadores)` | Coordina el cálculo y muestra las distancias Manhattan |
| `clasificar_jugador_por_direccion(jugador, jugador_con_pelota, posibles_pases)` | Clasifica a un jugador según la dirección relativa al portador |
| `insertar_menor_distancia(jugador, dist_jugador, dist_actual, lista)` | Inserta al jugador en la posición correcta según distancia |
| `menu_pases(jugador_con_pelota, posibles_pases, jugadores)` | Muestra las opciones de pase y permite ejecutar uno |
| `detectar_pases(jugadores, cancha)` | Coordina el análisis y muestra los pases posibles |
| `camino_libre_al_arco(jugador, cancha)` | Evalúa si un delantero tiene camino libre; retorna `True`/`False` |
| `detectar_camino_libre(jugadores, cancha)` | Recorre los delanteros y muestra el resultado para cada uno |
| `controlador_opciones(cancha, jugadores_en_cancha, jugadores)` | Loop principal del menú de opciones |
| `main()` | Punto de entrada del programa |

**Funciones de presentación:**

| Función | Descripción |
|---|---|
| `mostrar_cancha(cancha)` | Imprime la matriz con índices de fila y columna |
| `mostrar_menu()` | Muestra el menú principal |
| `mostrar_lista_jugadores(jugadores)` | Tabla con todos los jugadores registrados |
| `mostrar_menu_movimientos(jugador)` | Menú de dirección de movimiento |
| `mostrar_distancia_todos(jugador_pelota, distancias)` | Tabla de distancias Manhattan |
| `mostrar_jugadores_cercanos(jugador_pelota, cercanos)` | Muestra los jugadores más próximos a la pelota |
| `mostrar_lista_posibles_pases(jugador, posibles_pases)` | Muestra los pases disponibles por dirección |
| `mensaje_ok(texto)` | Mensaje de éxito en verde ✅ |
| `mensaje_error(texto)` | Mensaje de error en rojo ❌ |
| `mensaje_advertencia(texto)` | Mensaje de advertencia en amarillo ⚠️ |
| `mensaje_info(texto)` | Mensaje informativo en azul ℹ️ |

---

## Manejo de errores

| Situación | Mensaje |
|---|---|
| Posición fuera de la cancha | `Fila/Columna X fuera de la cancha` |
| Celda ya ocupada | `Celda (fila, columna) ya ocupada` |
| Rol inválido | `Rol 'X' inválido` |
| Equipo inválido | `Equipo 'X' inválido` |
| Pelota duplicada | `Ya hay un jugador con la pelota` |
| Movimiento fuera de límites o celda ocupada | `Movimiento inválido: posición fuera de límites o celda ocupada` |
| Ningún jugador tiene la pelota | `Ningun jugador tiene la pelota` / `Nadie tiene el balón` |
| Sin pases disponibles | `No hay pases disponibles` |
| Entrada no numérica | `Ingrese un número válido` |

Ante cualquier error se muestra un mensaje descriptivo con color y el programa continúa en ejecución.