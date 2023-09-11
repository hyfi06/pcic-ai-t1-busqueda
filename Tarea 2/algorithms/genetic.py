from typing import Set, Callable, TypeVar, List, Tuple, Optional
from algorithms.models import Individual
import random


U = TypeVar('U', bound=Individual)


def crossing(parent_1: U, parent_2: U) -> Tuple[U, U]:
    chromosome_1 = parent_1.get_chromosome(parent_1.variables)
    chromosome_2 = parent_2.get_chromosome(parent_2.variables)

    cross_point = random.randrange(0, len(chromosome_1))
    child_1 = chromosome_1[:cross_point]+chromosome_2[cross_point:]
    child_2 = chromosome_2[:cross_point]+chromosome_1[cross_point:]

    return (parent_1.__class__(chromosome=child_1), parent_1.__class__(chromosome=child_2))


def mutate(individual: U) -> U:
    individual.__mutate__()
    return individual


def genetic(
    initial_population: List[U],
    fitness: Callable[[U], int | float],
    goal_test: Callable[[U], bool],
    generations: int,
    fist_solution: Optional[bool] = True
) -> Set[str]:
    solutions: Set[str] = set()
    population: List[U] = initial_population
    population_size = len(initial_population)
    max_fitness = fitness(population[0])
    while generations > 0:
        parents: List[U] = list()
        while len(parents) == population_size:
            i_1, i_2 = random.choices(population=population, k=2)
            parents.append(max([i_1, i_2], key=fitness))

        children: List[U] = list()
        for i in range(0, len(parents), 2):
            child_1, child_2 = crossing(parents[i], parents[i+1])
            children.extend([child_1, child_2])
        population = [mutate(child) for child in children]
        generations -= 1
        max_individual = max(population, key=fitness)

        if max_fitness < fitness(max_individual) and goal_test(max_individual):
            solutions.add(str(max_individual))
            if fist_solution:
                break

    return solutions
