# Tarea 3

## Ejecución

### Repositorio

[https://github.com/hyfi06/pcic-ai241/tree/tarea-3](https://github.com/hyfi06/pcic-ai241/tree/tarea-3)

```bash
git clone https://github.com/hyfi06/pcic-ai241.git

git checkout tarea-3
```

### Python version

- Python 3.10.6

### En local

```bash
python3 minimax_vs_minimax.py
python3 expectimax_vs_expectimax.py
python3 minimax_vs_expectimax.py
```

## Implementaciones

### Minimax con podado alfa-beta

La implementación se encuentra en la carpeta [Tarea 3/algorithms/minimax.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-3/Tarea%203/algorithms/minimax.py)

### Expectimax

La implementación se encuentra en la carpeta [Tarea 3/algorithms/expectimax.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-3/Tarea%203/algorithms/expectimax.py)

## Resultados

### minimax vs minimax

Los resultado en la carpeta [Tarea 3/result](https://github.com/hyfi06/pcic-ai241/tree/tarea-3/Tarea%203/results), los archivos tiene el prefijo m_vs_m

```
-------------
| O | O | X |
-------------
| X | X | O |
-------------
| O | X | X |
-------------

Tie
```

Resultados: 5 empates

### minimax vs expectimax

Los resultado en la carpeta [Tarea 3/result](https://github.com/hyfi06/pcic-ai241/tree/tarea-3/Tarea%203/results), los archivos tiene el prefijo m_vs_e

```
X: Expectimax vs O: Minimax
-------------
| O | X | O |
-------------
| O | X | X |
-------------
| X | O | X |
-------------

Tie
```

```
X: Minimax vs O: Expectimax
-------------
| O | O | X |
-------------
| X | X | O |
-------------
| O | X | X |
-------------

Tie
```

Resultados: 5 empates

### expectimax vs expectimax

Los resultado en la carpeta [Tarea 3/result](https://github.com/hyfi06/pcic-ai241/tree/tarea-3/Tarea%203/results), los archivos tiene el prefijo e_vs_e

```
-------------
| O | X | O |
-------------
| O | X | X |
-------------
| X | O | X |
-------------

Tie
```

Resultados: 5 empates
