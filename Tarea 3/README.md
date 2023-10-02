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

Hay 3 modelos que satisface la fórmula. Como $A$ y $D$ no aparecen en la formula, entonces en total hay $3*2^2=12$ modelos en total.

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

#### g) $C \vee (\neg A \wedge \neg B) \equiv A \rarr C\wedge B\rarr C$

Sae $w$ tal que $I(C \vee (\neg A \wedge \neg B),w)=1$. Entonces, $I(C,w)=1$ o $I(\neg A \wedge \neg B,w)=1$

Si $I(C,w) = 1$, $I(A\rarr C,w) = 1$ y $I(B\rarr C,w)=1$. Por lo que, $I(A \rarr C\wedge B\rarr C, w)=1$.

Si $I(\neg A \wedge \neg B, w)=1$, entonces $I(A)=0$ y $I(B)=0$. Por lo que, $I(A\rarr C,w) =1 $ y $I(B\rarr C,w)=1$. Así, $I(A \rarr C\wedge B\rarr C, w)=1$.

En ambos casos, $I(A \rarr C\wedge B\rarr C, w)=1$.

Por lo que, $C \vee (\neg A \wedge \neg B) \models A \rarr C\wedge B\rarr C$

Sea $w$ tal que $I(A \rarr C\wedge B\rarr C, w)=1$. Entonces $I(A\rarr C,w) = 1$ y $I(B\rarr C,w)=1$. Por lo que, $I(\neg A\vee C,w) = 1$ y $I(\neg B\vee C,w)=1$.

Si $I(C,w)=1$, entonces $I(C \vee (\neg A \wedge \neg B),w)=1$.

Si $I(C,w)=0$, entonces $I(\neg A,w)=1$ y $I(\neg B,w)=1$. Por lo que, $I(C \vee (\neg A \wedge \neg B),w)=1$.

En ambos casos $I(C \vee (\neg A \wedge \neg B),w)=1$

Entonces, $A \rarr C\wedge B\rarr C\models C \vee (\neg A \wedge \neg B)$

Por lo tanto, $C \vee (\neg A \wedge \neg B) \equiv A \rarr C\wedge B\rarr C$

#### h) $(A\vee B)\wedge (\neg C \vee \neg D \vee E)\models A \vee B$

Verdadero.

Veamos que $\{(A\vee B)\wedge (\neg C \vee \neg D \vee E),\neg(A \vee B)\}$ no es satisfactible.

Sea $w$ un modelo. Si $I((A\vee B)\wedge (\neg C \vee \neg D \vee E),w)=1$, $I(A\vee B,w)=1$. Por lo que, $I(\neg(A\vee B),w)=0$.

Entonces el conjunto no es satisfactible.

#### i) $(A\vee B)\wedge (\neg C \vee \neg D \vee E)\models (A \vee B)\wedge (\neg D \vee E)$

Falso.

Sae $w=\{A:V,B:V,C:F,D:V,E:F\}$.

| $(A$ | $\vee$ | $B)$ | $\wedge$ | $(\neg$ | $C$ | $\vee$ | $\neg$ | $D$ | $\vee$ | $E)$ |
| ---- | ------ | ---- | -------- | ------- | --- | ------ | ------ | --- | ------ | ---- |
| V    | V      | V    | **V**    | V       | F   | V      | F      | V   | F      | F    |

| $(A$ | $\vee$ | $B)$ | $\wedge$ | $(\neg$ | $D$ | $\vee$ | $E)$ |
| ---- | ------ | ---- | -------- | ------- | --- | ------ | ---- |
| V    | V      | V    | **F**    | F       | V   | F      | F    |

#### j) $(A\vee B) \wedge \neg (A\rarr B)$

Verdadero.

Sae $w=\{A:V,B:F\}$.

| $(A$ | $\vee$ | $B)$ | $\wedge$ | $\neg$ | $(A$ | $\rarr$ | $B)$ |
| ---- | ------ | ---- | -------- | ------ | ---- | ------- | ---- |
| V    | V      | F    | **V**    | V      | V    | F       | F    |

#### k) $(A\lrarr B )\wedge (\neg A\vee B)$

| $(A$ | $\lrarr$ | $B)$ | $\wedge$ | $(\neg$ | $A$ | $\vee$ | $B)$ |
| ---- | -------- | ---- | -------- | ------- | --- | ------ | ---- |
| V    | V        | V    | **V**    | F       | V   | V      | V    |

### l)

Verdadero.

Por inducción sobre el número de símbolos proposicionales adicionales a $A$, $B$, $C$.

Paso base $n=0$

| $A$ | $B$ | $C$ | $(A\lrarr B)$ | $(A\lrarr B)\lrarr C$ |
| --- | --- | --- | ------------- | --------------------- |
| V   | V   | V   | V             | V                     |
| V   | V   | F   | V             | F                     |
| V   | F   | V   | F             | F                     |
| V   | F   | F   | F             | V                     |
| F   | V   | V   | F             | F                     |
| F   | V   | F   | F             | V                     |
| F   | F   | V   | V             | V                     |
| F   | F   | F   | V             | F                     |

Existen 4 modelos que satisface $(A\lrarr B)$ y 4 modelos que satisface $(A\lrarr B)\lrarr C$.

H.I.: Supongamos para $n=k$ que tiene la misma cantidad de modelos.

Sean $A_1$, $A_2$,..., $A_k$, $A_{k+1}$, los símbolos proposicionales adicionales a $A$, $B$, $C$.
Por hipótesis de inducción, existen la misma cantidad de modelos para $(A\lrarr B)$ y $(A\lrarr B)\lrarr C$ con $A$, $B$, $C$, $A_1$, $A_2$,..., $A_k$.
Al agregar $A_{k+1}$, se multiplica por 2 la cantidad de modelos posibles. Ya que como $A_{k+1}$ no aparece en $(A\lrarr B)$ ni $(A\lrarr B)\lrarr C$, si w es un modelo que satisface alguna de las dos fórmulas, $w\cup\{A_{k+1}:True\}$ y $w\cup\{A_{k+1}:Falso\}$ son también modelos.

Entonces, existen la misma cantidad de model para $(A\lrarr B)$ y $(A\lrarr B)\lrarr C$ con $A$, $B$, $C$, $A_1$, $A_2$,..., $A_k$, $A_{k+1}$.

Por el principio de inducción, el se cumple para toda $n$.

### 7.18

$[(Food \rarr Party)\vee(Drinks\rarr Party)] \rarr [(Food \wedge Drinks)\rarr Party]$

#### a)

| $[(Food$ | $\rarr$ | $Party)$ | $\vee$ | $(Drinks$ | $\rarr$ | $Party)]$ | $\rarr$ | $[(Food$ | $\wedge$ | $Drinks)$ | $\rarr$ | $Party]$ |
| -------- | ------- | -------- | ------ | --------- | ------- | --------- | ------- | -------- | -------- | --------- | ------- | -------- |
| V        | V       | V        | V      | V         | V       |           | V       |          | V        |           | V       |
| V        | V       | V        | V      | F         | V       |           | V       |          | F        |           | V       |
| V        | F       | F        | F      | V         | F       |           | V       |          | V        |           | F       |
| V        | F       | F        | V      | F         | V       |           | V       |          | F        |           | V       |
| F        | V       | V        | V      | V         | V       |           | V       |          | F        |           | V       |
| F        | V       | V        | V      | F         | V       |           | V       |          | F        |           | V       |
| F        | V       | F        | V      | V         | F       |           | V       |          | F        |           | V       |
| F        | V       | F        | V      | F         | V       |           | V       |          | F        |           | V       |

Es válida.

#### b)

$[(Food \rarr Party)\vee(Drinks\rarr Party)] \rarr [(Food \wedge Drinks)\rarr Party]$

$[(\neg Food \vee Party)\vee(\neg Drinks\vee Party)] \rarr [\neg (Food \wedge Drinks)\vee Party]$

$(\neg Food \vee Party\vee\neg Drinks\vee Party) \rarr (\neg Food \vee \neg Drinks \vee Party)$

Se confirma la a) ya que el consecuente de la implicación es el antecedente quitando la redundancia de Party.

#### c)

$\vdash (\neg Food \vee Party\vee\neg Drinks\vee Party) \rarr (\neg Food \vee \neg Drinks \vee Party)$

$\{\neg Food \vee Party\vee\neg Drinks\vee Party\} \vdash \neg Food \vee \neg Drinks \vee Party$

Apliquemos resolución

$\{\neg Food \vee Party\vee\neg Drinks\vee Party, \neg(\neg Food \vee \neg Drinks \vee Party)\}$

$\{\neg Food \vee Party\vee\neg Drinks\vee Party,  Food \wedge  Drinks \wedge \neg Party\}$

$\{\neg Food \vee Party\vee\neg Drinks\vee Party,  Food,  Drinks, \neg Party\}$

$Food$, $\neg Food \vee Party\vee\neg Drinks\vee Party$ -> $Party\vee\neg Drinks\vee Party$

$\neg Party$, $Party\vee\neg Drinks\vee Party$ -> $\neg Drinks\vee Party$

Drinks, $\neg Drinks\vee Party$ -> $Party$

$Party$, $\neg Party$ -> False

Por lo tanto, no es satisfactible.

Entonces $\{\neg Food \vee Party\vee\neg Drinks\vee Party\} \vdash \neg Food \vee \neg Drinks \vee Party$

### 7.4

a) $\exists x (Parent(Joan,x)\wedge Female(x))$

b) $\exists^1 x (Parent(Joan,x)\wedge Female(x))$

c) $\exists^1 x Parent(Joan,x) \wedge \forall x (Parent(Joan,x) \rarr Female(x))$

d) $\exists^1 x (Parent(Joan,x) \wedge Parent(Kevin,x))$

e) $\exists x (Parent(Joan,x) \wedge Parent(Kevin,x))\wedge$ $\forall x (Parent(Joan,x) \rarr Parent(Kevin,x))$

### 8.10

a. $Occupation(Emily,Surgeon) \vee Occupation(Emily, Lawyer)$

