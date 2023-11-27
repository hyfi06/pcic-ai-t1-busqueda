from typing import Set, Callable, TypeVar, List, Tuple, Optional
from tools import read_data, timer, execution_time
import random as rnd

from models import Clase, Profesor, Individual
from genetic import genetic, Individual


class Asignacion(Individual):
    profesores: List[Profesor] = list()
    clases: List[Clase] = list()

    def get_asignaciones(self) -> List[Tuple[Clase, Profesor]]:
        return [
            (Asignacion.clases[i], Asignacion.profesores[j])
            for i, j in enumerate(self.variables)
        ]


def fitness(asignacion: Asignacion) -> float:
    conflictos = 0
    asignaciones = asignacion.get_asignaciones()
    horas = [0] * len(Asignacion.profesores)
    for i, (clase1, profesor1) in enumerate(asignaciones):
        horas[profesor1.id] += 1
        for clase2, profesor2 in asignaciones[i+1:]:
            if profesor1.id == profesor2.id and clase1.dia == clase2.dia:
                clases_profesor = [clase1, clase2]
                clases_profesor.sort(key=lambda x: x.horario[1])
                if clases_profesor[0].horario[1] > clases_profesor[1].horario[0]:
                    conflictos += 1
    for i, profesor in enumerate(Asignacion.profesores):
        if profesor.max_horas < horas[i]:
            conflictos += 1
    return 1/(1.0 * conflictos + 1)


def conflicts(asignacion: Asignacion):
    conflictos = []
    asignaciones = asignacion.get_asignaciones()
    horas = [0] * len(Asignacion.profesores)
    for i, (clase1, profesor1) in enumerate(asignaciones):
        horas[profesor1.id] += 1
        for clase2, profesor2 in asignaciones[i+1:]:
            if profesor1.id == profesor2.id and clase1.dia == clase2.dia:
                clases_profesor = [clase1, clase2]
                clases_profesor.sort(key=lambda x: x.horario[1])
                if clases_profesor[0].horario[1] > clases_profesor[1].horario[0]:
                    conflictos.append((
                        i, profesor1.id, profesor2.id,
                        str(clase1), str(clase2)
                    ))
    for i, profesor in enumerate(Asignacion.profesores):
        if profesor.max_horas < horas[i]:
            conflictos.append((
                i, profesor.id, profesor.max_horas, horas[i]
            ))
    return conflictos


def get_initial_population(length: int) -> List[Asignacion]:
    population = [
        Asignacion(
            values=[
                rnd.choice(domain)
                for domain in Asignacion.domains
            ]
        )
        for _ in range(length)
    ]
    return population


@execution_time
def main():
    file = './Plantilla.xlsx'
    profesores, clases = read_data(file)
    Asignacion.domains = [
        clase.profesores
        for clase in clases
    ]
    Asignacion.profesores = profesores
    Asignacion.clases = clases
    initial_population = get_initial_population(len(clases)//2)
    res = genetic(
        initial_population=initial_population,
        fitness=fitness,
        goal_test=lambda x: fitness(x) == 1,
        timer=timer(3*60),
    )

    print(res)


if __name__ == "__main__":
    main()
