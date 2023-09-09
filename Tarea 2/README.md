# Tarea 2

## Runtime

- Python 3.10.6

## Ejecución

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
