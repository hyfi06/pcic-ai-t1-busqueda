from typing import List, Tuple, Optional, Generic, TypeVar
from abc import abstractproperty

import random


class Clase:
    def __init__(
        self,
        id: int,
        nombre: str,
        dia: str,
        horario: Tuple[int, int],
        profesores: list[int],
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.dia = dia
        self.horario = horario
        self.profesores = profesores

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id}, {self.dia} {self.horario[0]}-{self.horario[1]})"


class Profesor:
    def __init__(
        self,
        id: int,
        nombre: str,
        horas: int
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.max_horas = horas

    def __str__(self) -> str:
        return f"{self.nombre} ({self.id})"


T = TypeVar('T')


class State(Generic[T]):
    def __init__(self, values: List[T], domain_per_variable: List[List[T]]) -> None:
        self.variables: List[T] = values
        self.domain_per_variable: List[List[T]] = domain_per_variable

    def variable_order(self) -> List[int]:
        idx_domains: List[tuple[int, List[T]]] = list(
            enumerate(self.domain_per_variable))
        idx_domains.sort(key=lambda enum: len(enum[1]))
        return [
            idx for (idx, domain) in idx_domains
            if len(domain)
        ]

    @abstractproperty
    def is_valid(self) -> bool:
        return True

    def __str__(self) -> str:
        return self.variables.__str__()


class Individual(State[int]):
    domains: List[List[int]] = list()

    def __init__(
        self,
        values: Optional[List[int]] = None,
        domain_per_variable: Optional[List[List[int]]] = None,
        chromosome: Optional[str] = None
    ) -> None:
        if not domain_per_variable:
            domain_per_variable = self.domains
        if chromosome is not None and values is not None:
            raise ValueError(
                'Cannot provide both arguments chromosome and values')
        if chromosome:
            values = self.values_from_chromosome(chromosome)
            super().__init__(values, domain_per_variable)
        elif values:
            super().__init__(values, domain_per_variable)
        else:
            raise ValueError('values or chromosome are necessary')

    @classmethod
    def get_chromosome(cls, values) -> str:
        chromosome: str = ''
        for idx, value in enumerate(values):
            gen: str = bin(value - min(cls.domains[idx]))[2:]
            gen = gen.zfill(len(
                bin(max(cls.domains[idx]) -
                    min(cls.domains[idx]))[2:]
            ))
            chromosome += gen

        return chromosome

    @classmethod
    def values_from_chromosome(cls, chromosome: str) -> List[int]:
        i = 0
        j = 0
        values = []
        while i < len(chromosome):
            max_value = max(cls.domains[j])
            min_value = min(cls.domains[j])
            gen_size = len(bin(max_value - min_value)[2:])
            gen = chromosome[i:i + gen_size]
            value = min_value + (int(gen, 2) % (max_value-min_value+1))

            values.append(value)
            j += 1
            i += gen_size
        return values

    def __mutate__(self) -> None:
        chromosome: List[str] = list(self.get_chromosome(self.variables))
        p_m: float = 1.0 / len(chromosome)
        for idx, value in enumerate(chromosome):
            if p_m > random.random():
                chromosome[idx] = str(1 - int(value))
        self.variables = self.values_from_chromosome(''.join(chromosome))
