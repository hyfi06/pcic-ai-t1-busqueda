# Tarea 2

## Ejecución

### Repositorio

[https://github.com/hyfi06/pcic-ai241/tree/tarea-2](https://github.com/hyfi06/pcic-ai241/tree/tarea-2)

```bash
git clone https://github.com/hyfi06/pcic-ai241.git

git checkout tarea-2
```

### Python version

- Python 3.10.6

### En local

```bash
python3 file args
```

### En servidor

```bash
nohup python3 -u file args > resultados/algorithm_problem_n_$(date +"%Y_%m_%d_%H_%M_%S").txt &
```

### Debug

Insertar las siguiente linea en el lugar que se quiere parar la ejecución

```python
import pdb; pdb.set_trace()
```

## Implementaciones

### Búsqueda con backtracking, filtrado y ordenamiento

La implementación se encuentra en la carpeta [Tarea 2/algorithms/backtracking.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/algorithms/backtracking.py)

#### Complejidad computacional

La complejidad computacional de este algoritmo en el peor de los casos es igual a DFS, es decir, $O(b^m)$ en tiempo y $O(bm)$ en espacio. Donde, $b$ es el factor de ramificación y $m$ la profundidad máxima.

El ordenamiento nos sirve para enfocar la búsqueda a las ramas más cortas de explorar, pero no garantiza en todos los casos encontrar una solución. Y la poda o filtrado, puede disminuir b, pero no para todos los nodos. Así que en el peor caso se sigue explorando la mayor parte del árbol.

#### N reinas con N=8,50,100

Implementación en [bt_nQueens.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/bt_nQueens.py).

```bash
python3 bt_nQueens.py 8
python3 bt_nQueens.py 50
python3 bt_nQueens.py 100
```

Los resultados se encuentra en:

- [bt_nQueens_8_2023_09_08_20_08_15.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_nQueens_8_2023_09_08_20_08_15.txt)
- [bt_nQueens_50_2023_09_08_20_10_06.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_nQueens_50_2023_09_08_20_10_06.txt)
- [bt_nQueens_100_2023_09_08_20_10_19.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_nQueens_100_2023_09_08_20_10_19.txt)

La solución es un array que modela cada columna del tablero y el número es el renglón donde se encuentra la reina de esa columna.

Los mejores tiempos reportados fuero:

| n   | Tiempo      |
| --- | ----------- |
| 8   | 0.03s       |
| 50  | 14min 2.87s |
| 100 | 13.38s      |

Con un filtrado muy adecuado, se pudo reducir a estos tiempos.

#### Problema de la mochila

Implementación en [bt_ks.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/bt_ks.py).

```bash
python3 bt_ks.py ../Tarea\ 1/ks_19_0
python3 bt_ks.py ../Tarea\ 1/ks_10000_0
```

Los resultados se encuentran en:

- [bt_ks_19_2023_09_08_20_50_09.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_ks_19_2023_09_08_20_50_09.txt)
- [bt_ks_10000_2023_09_08_20_51_39.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_ks_10000_2023_09_08_20_51_39.txt)

La solución muestra un array de tuplas que en su primera entrada sería el número de objecto seguido una tupla de valor, peso.

Los mejores tiempos reportados fuero:

| Items | Tiempo      |
| ----- | ----------- |
| 19    | 0.001s      |
| 10000 | 3min 39.63s |

Deje correr por casi 3 días el algoritmo para con ks_10000_0 y la mejor solución encontrada fue:

```
V:1099893 W:999994
Items:
[(568, (76140, 69221)), (1824, (61650, 56051)), (2192, (49960, 45426)), (2641, (115117, 104666)), (2827, (4562, 4148)), (2946, (41755, 37964)), (3003, (92264, 83877)), (3023, (177323, 161215)), (6113, (8, 9)), (7055, (109027, 99123)), (7498, (22, 21)), (7577, (108657, 98789)), (8034, (69271, 62979)), (9431, (14388, 13082)), (9756, (179749, 163423))]
```

#### Coloreado

Implementación en [bt_gc.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/bt_gc.py).

```bash
python3 bt_gc.py gc_50_7
python3 bt_gc.py gc_1000_9
```

Los resultados se encuentran en:

- [bt_gc_50_2023_09_08_21_14_59.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_gc_50_2023_09_08_21_14_59.txt)
- [bt_gc_1000_2023_09_08_21_15_36.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_gc_1000_2023_09_08_21_15_36.txt)

Donde la solución es un array que representa cada nodo y el valor es el número de color que se usa.

Los mejores tiempos reportados fuero:

| Nodos | Tiempo     | Colores |
| ----- | ---------- | ------- |
| 50    | 0.03s      | 15      |
| 1000  | 2min 40.93 | 303     |

#### Comentarios sobre backtracking

Es muy tardado, pero con un buen filtrado y ordenamiento, puedes dirigirlo bastante bien a una solución. Pero esto requiere tiempo y más dominio del problema.

Funciona mejor, cuando te interesa conocer todas las soluciones y no te importa el tiempo. Con el filtrado y ordenamiento lo puedes usar para encontrar una solución, pero suele ser subóptima (como DFS).

### Búsqueda tabú

La implementación se encuentra en [Tarea 2/algorithms/taboo_search.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/algorithms/taboo_search.py).

#### Complejidad computacional

A tiempo infinito, búsqueda tabú podría terminar de recorrer todo el árbol de búsqueda. Además, también dependerá de la complejidad computacional del vecindario.
Sería $O(vb^m)$ donde v es el tamaño del vecindario.

#### N reinas con N=8,50,100

Implementación en [ts_nQueens.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/ts_nQueens.py).

```bash
python3 ts_nQueens.py 8
python3 ts_nQueens.py 50
python3 ts_nQueens.py 100
```

Los resultados se encuentra en:

- [ts_nQueens_8_2023_09_08_21_40_41.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_nQueens_8_2023_09_08_21_40_41.txt)
- [ts_nQueens_50_2023_09_08_21_40_52.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_nQueens_50_2023_09_08_21_40_52.txt)
- [ts_nQueens_100_2023_09_08_21_41_01.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_nQueens_100_2023_09_08_21_41_01.txt)

La solución es un array que modela cada columna del tablero y el número es el renglón donde se encuentra la reina de esa columna.

Los mejores tiempos reportados fuero:

| n   | Tiempo       |
| --- | ------------ |
| 8   | 0.09s        |
| 50  | 2min 29.46s  |
| 100 | 36min 36.35h |

#### Problema de la mochila

Implementación en [ts_ks.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/ts_ks.py).

```bash
python3 ts_ks.py ../Tarea\ 1/ks_19_0
python3 ts_ks.py ../Tarea\ 1/ks_10000_0
```

Los resultados se encuentran en:

- [ts_ks_19_2023_09_08_23_35_28.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_ks_19_2023_09_08_23_35_28.txt)
- [ts_ks_10000_2023_09_08_23_35_32.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_ks_10000_2023_09_08_23_35_32.txt)

La solución muestra un array de tuplas que en su primera entrada sería el número de objecto seguido una tupla de valor, peso.

Los mejores tiempos reportados fuero:

| Items | Tiempo     |
| ----- | ---------- |
| 19    | 0.003s     |
| 10000 | 1min 4.07s |

#### Coloreado

Implementación en [ts_gc.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/ts_gc.py).

```bash
python3 ts_gc.py gc_50_7
python3 ts_gc.py gc_1000_9
```

Los resultados se encuentran en:

- [ts_gc_50_2023_09_09_01_51_16.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/bt_gc_50_2023_09_08_21_14_59.txt)
- [ts_gc_1000_2023_09_09_01_50_39.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_gc_50_2023_09_09_01_51_16.txt)

Donde la solución es un array que representa cada nodo y el valor es el número de color que se usa.

Los mejores tiempos reportados fuero:

| Nodos | Tiempo     | Colores |
| ----- | ---------- | ------- |
| 50    | 0.01s      | 36      |
| 1000  | 1min 0.85s | 691     |

Los algoritmos se dejó correr 1 días y las mejores coloraciones que llegaron fueron 14 colares, 325 colores respectivamente.

#### [Eggholder](https://www.sfu.ca/~ssurjano/egg.html)

Implementación en [ts_eh.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/ts_eh.py).

```bash
python3 ts_eh.py
```

Los resultados se encuentran en:

- [ts_eh_2023_09_11_17_39_17.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/ts_eh_2023_09_11_17_39_17.txt)

Donde la soluciones encontradas son las coordenadas x1, x2 y el valor de la función en ese punto.

Los mejores tiempos reportados fuero en 3 min y 25.16s en el cual se encontró el sub óptimo

```
x1:506.88000000000017 y:399.36
Value: -937.9785290110033
```

Los algoritmos se dejó correr 1 días y las mejores coloraciones que llegaron fueron 14 colares, 325 colores respectivamente.

#### Comentarios sobre búsqueda tabú

En las implementaciones que se hicieron suele ser rápido, pero se debe escoger los vecinos. En varios problemas adapté los vecinos a un conjunto más manejable para que no tardara de realizar las iteraciones. Por otra parte, alguna implementación mal generada con muchos vecinos, tube que lidiar con el espacio en memoria, llegando a tener hasta 12G de vecinos.

Con vecinos controlados, resulta rápido. Pero aumenta la complejidad y el conocimiento del dominio para hacer una implementación manejable.

### Algoritmo genético

La implementación se encuentra en [Tarea 2/algorithms/genetic.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/algorithms/genetic.py).

#### Complejidad computacional

El cada paso se escogen $\mu$ padres por medio de 2-torneos, luego se recombinan de 2 en dos. se realizan $\mu$ mutaciones para generar la nueva población.

Por lo que la complejidad estará dada por el tamaña de la población $\mu$ y la complejidad de la función de actitud $\phi$. En total $O(\mu\phi)$.

#### N reinas con N=8,50,100

Implementación en [gen_nQueens.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/gen_nQueens.py).

```bash
python3 gen_nQueens.py 8
python3 gen_nQueens.py 50
python3 gen_nQueens.py 100
```

Los resultados se encuentra en:

- [gen_nQueens_8_2023_09_10_23_38_52.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_nQueens_8_2023_09_10_23_38_52.txt)
- [gen_nQueens_50_2023_09_10_23_55_57.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_nQueens_50_2023_09_10_23_55_57.txt)
- [gen_nQueens_100_2023_09_10_23_56_02.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_nQueens_100_2023_09_10_23_56_02.txt)

La solución es un array que modela cada columna del tablero y el número es el renglón donde se encuentra la reina de esa columna.

Los mejores tiempos reportados fuero:

| n   | Tiempo            | Conflictos(aptitud) |
| --- | ----------------- | ------------------- |
| 8   | 0.09s             | 0                   |
| 50  | 7hrs (No terminó) | 2 (3hrs)            |
| 100 | 7hrs (No terminó) | 3 (4hrs)            |

Para 50 y 100, no logró completar las condiciones en 7hrs.

- Para 50 el mejor individuo que encontró tenia 2 conflictos, la encontró a las 3hrs en la generación 207135
- Para 100 el mejor individuo que encontró tenia 3 conflictos, la encontró a las 3hrs en la generación 40585

#### Problema de la mochila

Implementación en [gen_ks.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/gen_ks.py).

```bash
python3 gen_ks.py../Tarea\ 1/ks_19_0
python3 gen_ks.py ../Tarea\ 1/ks_10000_0
```

Los resultados se encuentran en:

- [gen_ks_19_2023_09_11_00_52_04.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_ks_19_2023_09_11_00_52_04.txt)
- [gen_ks_10000_2023_09_11_09_29_46.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_ks_10000_2023_09_11_09_29_46.txt)

La solución muestra un array de tuplas que en su primera entrada sería el número de objecto seguido una tupla de valor, peso.

Los mejores tiempos reportados fuero:

| Items | Tiempo            |
| ----- | ----------------- |
| 19    | 2.61s             |
| 10000 | 10hs (No terminó) |

- Para el de 10000 objetos, el individuo mas óptimo lo encontró en 3 minutos, en la generación 38. Pero aún había espacio en la mochila.

La realizar las cruzas, los individuos nuevos han de haber superado el peso de la mochila y por eso ya no se registraron como candidatos. Esta propiedad se ha haber heredado en las siguientes generaciones por lo que ya no se pudo encontrar otra mejor solución.

#### Coloreado

Implementación en [gen_gc.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/gen_gc.py).

```bash
python3 gen_gc.py gc_50_7
python3 gen_gc.py gc_1000_9
```

Los resultados se encuentran en:

- [gen_gc_50_2023_09_11_01_06_37.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_gc_50_2023_09_11_01_06_37.txt)
- [gen_gc_1000_2023_09_11_09_29_19.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_gc_1000_2023_09_11_09_29_19.txt)

Donde la solución es un array que representa cada nodo y el valor es el número de color que se usa.

Los mejores tiempos reportados fuero:

| Nodos | Tiempo             | Colores |
| ----- | ------------------ | ------- |
| 50    | 3.66s              | 27      |
| 1000  | 13hrs (No terminó) |         |

El mejor resultado hasta el momento para el 1000 vértices es la generación: 6115 con 595 conflictos. El algoritmo no se ha estancado, reduce aproximadamente un conflicto cada 20 min.

#### [Eggholder](https://www.sfu.ca/~ssurjano/egg.html)

Implementación en [gen_eh.py](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/gen_eh.py).

```bash
python3 gen_eh.py
```

Los resultados se encuentran en:

- [gen_eh_2023_09_11_18_02_20.txt](https://github.com/hyfi06/pcic-ai241/blob/tarea-2/Tarea%202/resultados/gen_eh_2023_09_11_18_02_20.txt)

Donde la soluciones encontradas son las coordenadas x1, x2 y el valor de la función en ese punto.

Los mejores tiempos reportados fue 0.4s en el cual se encontró el sub óptimo en la generación 163

```
x1:511.99 x2:404.22
Value: -959.6067814165801
```

El algoritmo siguió corriendo durante 5hrs pero no se logró mejorar.

#### Comentarios sobre algoritmo genético

Muy fácil de implementar sin involucrar complejidad del dominio. Lo cual lo hace veloz para encontrar subóptimos. Pero la falta implementación del dominio del problema, hace que no se pueda guiar y evitar que se estanque. Por lo que le costó encontrar solución a los problemas discretos.
