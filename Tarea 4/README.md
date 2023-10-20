# Tarea 4

## Instalación

### Repositorio

[https://github.com/hyfi06/pcic-ai241/tree/tarea-4](https://github.com/hyfi06/pcic-ai241/tree/tarea-4)

```bash
git clone https://github.com/hyfi06/pcic-ai241.git

git checkout tarea-4
```

### Python version

- Python 3.10.6

### Entorno virtual

```bash
cd Tarea\ 4
python3 -m venv venv
source venv/bin/activate
```

### Instalación de dependencias

```
pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución

### Problema de la alarma

Implentación en https://github.com/hyfi06/pcic-ai241/blob/tarea-4/Tarea%204/alarma.py

```bash
python3 alarma.py
```

Resultado:

```
P(Burglary | JohnCalls=+j, MaryCalls=+m):
+-------+----------+
| B     |   phi(B) |
+=======+==========+
| B(-b) |   0.7158 |
+-------+----------+
| B(+b) |   0.2842 |
+-------+----------+

P(Earthqk | JohnCalls=+j, MaryCalls=+m):
+-------+----------+
| E     |   phi(E) |
+=======+==========+
| E(-e) |   0.8239 |
+-------+----------+
| E(+e) |   0.1761 |
+-------+----------+

P(JohnCalls | MaryCalls=-m):
+-------+----------+
| J     |   phi(J) |
+=======+==========+
| J(-j) |   0.9494 |
+-------+----------+
| J(+j) |   0.0506 |
+-------+----------+

Están d-separados de "Burglary" al observar "Alarm": {'B': {'E', 'B'}}
```

### Problema Barley

Modelo preliminar para cebada desarrollado en el marco del proyecto: "Producción de cerveza a partir de cebada cervecera danesa cultivada sin el uso de pesticidas" de Kristian Kristensen, Ilse A. Rasmussen y otros.

https://www.bnlearn.com/bnrepository/discrete-medium.html#barley

![Red](https://www.bnlearn.com/bnrepository/barley/barley.svg)

```bash
python3 barley.py
```

Queries: https://github.com/hyfi06/pcic-ai241/blob/tarea-4/Tarea%204/barley.py

Resultado:

```
Nodos:
['jordtype', 'komm', 'nedbarea', 'nmin', 'aar_mod', 'forfrugt', 'potnmin', 'jordn', 'pesticid', 'exptgens', 'mod_nmin', 'ngodnt', 'nopt', 'ngodnn', 'ngodn', 'nprot', 'saatid', 'rokap', 'dgv1059', 'sort', 'srtprot', 'nplac', 'dg25', 'ngtilg', 'ntilg', 'saamng', 'tkvs', 'saakern', 'partigerm', 'frspdag', 'jordinf', 'markgrm', 'antplnt', 'sorttkv', 'aks_m2', 'keraks', 'dgv5980', 'aks_vgt', 'srtsize', 'ksort', 'protein', 'udb', 'spndx', 'tkv', 'slt22', 's2225', 's2528', 'bgbyg']

Aristas:
[('jordtype', 'nmin'), ('jordtype', 'aar_mod'), ('jordtype', 'potnmin'), ('jordtype', 'exptgens'), ('jordtype', 'rokap'), ('komm', 'nedbarea'), ('komm', 'aar_mod'), ('nedbarea', 'nmin'), ('nmin', 'jordn'), ('nmin', 'mod_nmin'), ('aar_mod', 'jordn'), ('aar_mod', 'mod_nmin'), ('forfrugt', 'potnmin'), ('forfrugt', 'exptgens'), ('forfrugt', 'ngodnt'), ('potnmin', 'jordn'), ('jordn', 'ngodnn'), ('jordn', 'nprot'), ('jordn', 'ntilg'), ('pesticid', 'exptgens'), ('pesticid', 'nopt'), ('exptgens', 'ngodnt'), ('exptgens', 'nopt'), ('mod_nmin', 'ngodnt'), ('ngodnt', 'ngodn'), ('nopt', 'ngodnn'), ('ngodnn', 'ngodn'), ('ngodn', 'nprot'), ('ngodn', 'ngtilg'), ('nprot', 'protein'), ('saatid', 'dgv1059'), ('saatid', 'dg25'), ('saatid', 'frspdag'), ('rokap', 'dgv1059'), ('rokap', 'dgv5980'), ('dgv1059', 'aks_m2'), ('dgv1059', 'keraks'), ('dgv1059', 'protein'), ('dgv1059', 'bgbyg'), ('sort', 'srtprot'), ('sort', 'sorttkv'), ('sort', 'srtsize'), ('srtprot', 'protein'), ('nplac', 'ngtilg'), ('dg25', 'ngtilg'), ('ngtilg', 'ntilg'), ('ntilg', 'aks_m2'), ('ntilg', 'keraks'), ('ntilg', 'aks_vgt'), ('ntilg', 'spndx'), ('ntilg', 'tkv'), ('saamng', 'saakern'), ('tkvs', 'saakern'), ('saakern', 'antplnt'), ('partigerm', 'markgrm'), ('frspdag', 'jordinf'), ('jordinf', 'markgrm'), ('markgrm', 'antplnt'), ('antplnt', 'aks_m2'), ('sorttkv', 'aks_m2'), ('sorttkv', 'tkv'), ('aks_m2', 'keraks'), ('aks_m2', 'aks_vgt'), ('aks_m2', 'udb'), ('aks_m2', 'tkv'), ('keraks', 'ksort'), ('keraks', 'tkv'), ('keraks', 'slt22'), ('keraks', 's2225'), ('keraks', 's2528'), ('dgv5980', 'aks_vgt'), ('dgv5980', 'spndx'), ('dgv5980', 'bgbyg'), ('aks_vgt', 'ksort'), ('aks_vgt', 'udb'), ('aks_vgt', 'slt22'), ('aks_vgt', 's2225'), ('aks_vgt', 's2528'), ('srtsize', 'ksort'), ('srtsize', 'slt22'), ('srtsize', 's2225'), ('srtsize', 's2528'), ('ksort', 'protein'), ('ksort', 'spndx')]

P(keraks| slt22=x0_1, protein=x10_5_11_0)
+----------------+---------------+
| keraks         |   phi(keraks) |
+================+===============+
| keraks(x_13)   |        0.0777 |
+----------------+---------------+
| keraks(x13_15) |        0.3962 |
+----------------+---------------+
| keraks(x15_17) |        0.2782 |
+----------------+---------------+
| keraks(x17_19) |        0.1496 |
+----------------+---------------+
| keraks(x19_21) |        0.0980 |
+----------------+---------------+
| keraks(x21_23) |        0.0001 |
+----------------+---------------+
| keraks(x_23)   |        0.0001 |
+----------------+---------------+

P(nprot| aks_m2=x450_550, dgv5980=x15_25)
+-----------------+--------------+
| nprot           |   phi(nprot) |
+=================+==============+
| nprot(x_40)     |       0.0674 |
+-----------------+--------------+
| nprot(x40_60)   |       0.1881 |
+-----------------+--------------+
| nprot(x60_80)   |       0.2215 |
+-----------------+--------------+
| nprot(x80_100)  |       0.2140 |
+-----------------+--------------+
| nprot(x100_120) |       0.1527 |
+-----------------+--------------+
| nprot(x120_140) |       0.1556 |
+-----------------+--------------+
| nprot(x140_160) |       0.0005 |
+-----------------+--------------+
| nprot(x_160)    |       0.0001 |
+-----------------+--------------+

P(protein| spndx=x_7)
+---------------------+----------------+
| protein             |   phi(protein) |
+=====================+================+
| protein(x_9)        |         0.0737 |
+---------------------+----------------+
| protein(x9_0_9_5)   |         0.0649 |
+---------------------+----------------+
| protein(x9_5_10_0)  |         0.0959 |
+---------------------+----------------+
| protein(x10_0_10_5) |         0.1241 |
+---------------------+----------------+
| protein(x10_5_11_0) |         0.1402 |
+---------------------+----------------+
| protein(x11_0_11_5) |         0.1382 |
+---------------------+----------------+
| protein(x11_5_12_0) |         0.1194 |
+---------------------+----------------+
| protein(x_12_0)     |         0.2437 |
+---------------------+----------------+

Están D-separados de 'nprot' al observar 'protein': {'nprot': {'bgbyg', 'nedbarea', 'jordinf', 'keraks', 'ksort', 'potnmin', 'exptgens', 'dgv1059', 'jordtype', 'aks_vgt', 'ngtilg', 'antplnt', 'frspdag', 'sorttkv', 'mod_nmin', 'dgv5980', 'ngodn', 'aar_mod', 'saamng', 'slt22', 'saatid', 'forfrugt', 'jordn', 'nplac', 's2225', 'srtsize', 'sort', 'partigerm', 'spndx', 'rokap', 'nopt', 'ntilg', 'nprot', 'markgrm', 'nmin', 'ngodnn', 'aks_m2', 'pesticid', 'tkv', 's2528', 'dg25', 'srtprot', 'komm', 'udb', 'tkvs', 'saakern', 'ngodnt'}}
```
