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

## Ejercicios de Lógica

### 7.7

Como $A$, $B$, $C$, $D$ son los únicos proposiciones, existen $2^4$ modelos.

#### a) $B \vee C$

| B   | C   | $B \vee C$ |
| --- | --- | ---------- |
| V   | V   | V          |
| V   | F   | V          |
| F   | V   | V          |
| F   | F   | F          |

Hay 3 modelos que satisface la fórmula. Como $A$ y $D$ ocurren libres, entonces en total hay $3*2^2=12$ modelos en total.

#### b) $\neg A \vee \neg B \vee \neg C \vee \neg D$

La fórmula es equivalente a $\neg (A \wedge B \wedge C \wedge D)$.

Si un modelo no satisface la fórmula, entonces satisface $A\wedge B\wedge C\wedge D$, entonces el modelo es $s(A)=T$, $s(B)=T$, $s(C)=T$ y $s(D)=T$

Por lo que, todos los demás modelos satisfacen la fórmula. En total $2^4 -1 = 15$

#### c) $(A \rarr B)\wedge A \wedge \neg B \wedge C \wedge D$

Supongamos que $s$ una asignación de verdad que satisface la fórmula.

Entonces,

- $s(A \rarr B) = T$
- $s(A) = T$
- $s(\neg B) = T$
- $s(C) = T$
- $s(D) = D$

Pero $s(A) = T$ y $s(\neg B) = T$, por lo que $s(A\rarr B) = F$. Lo cual es una contradicción.

Por lo tanto no existe la asignación.

Entonces existen 0 modelos para la fórmula.

### 7.4

#### a) $False \models True$

Verdadero.

$\{False, \neg True\}$ no es satisfactible.

#### b) $True \models False$

Falso. $\{ True, \neg False\}$ es satisfactible. Sea $w=\{\}$, $I(True\wedge \neg False, w)=1$

##### c) $A\wedge B \models A \lrarr B$

Verdadero.

Sea w un modelo. Si $I(A\wedge B,w)=1$, entonces $I(A,w) = 1$ y $I(B,w)=1$. Por lo tanto, $I(A\lrarr B,w) = 1$.

##### d) $A\lrarr B \models A \vee B$

Falso. $\{A\lrarr B, \neg (A\vee B)\}$ es satisfactible.

Sae $w = \{A:F, B:F\}$. Entonces $I(A\lrarr B,w)= 1$ y $I(A\vee B,w)=0$. Por lo tanto, $I(\neg (A\vee B),w)=1$ y el conjunto es satisfactible.

#### e) $A\lrarr B \models \neg A \vee B$

Verdadero.

Veamos que $\{A\lrarr B, \neg (\neg A \vee B)\}$ no es satisfactible.

Si $I(\neg (\neg A \vee B),w) =1$, entonces $I(A\wedge \neg B,w) =1$. Por lo que, $I(A,w) =1$ y $I(B,w)=0$. Entonces $I(A\lrarr B,w)=0$.

Por lo que, el conjunto no es satisfactible.

#### f) $(A \wedge B) \rarr C \models (A \rarr C) \vee (B \rarr C)$

Verdadero.

Veamos que $\{(A \wedge B) \rarr C, \neg ((A \rarr C) \vee (B \rarr C))\}$ no es satisfactible.

Saea $w$ un modelo. Si $I(\neg ((A \rarr C) \vee (B \rarr C)),w) = 1$, entonces $I(\neg( A \rarr C),w) =1$ y $I(\neg (B \rarr C),w)=1$.

Entonces, $I(A\wedge \neg C,w) = 1$ y $I(B\wedge \neg C,w)=1$. Por lo tanto, $I(A,w)=1$, $I(B,w)=1$ y $I(C,w)=0$.

Entonces $I((A\wedge B)\rarr C)=0$. Por lo tanto el conjunto no es satisfactible.


