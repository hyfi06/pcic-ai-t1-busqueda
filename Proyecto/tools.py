from typing import Tuple, List, TypeAlias, Optional, Callable

import pandas as pd
import datetime
import time
import functools
import sys


from models import Profesor, Clase


def read_data(path: str) -> Tuple[List[Profesor], List[Clase]]:
    profesores = pd.read_excel(
        path,
        sheet_name='PROFESORES'
    )
    clases = pd.read_excel(
        path,
        sheet_name='CLASES',
    )
    profesores = [
        Profesor(
            id=row['id'],
            nombre=row['nombre'],
            horas=row['horas_max']
        )
        for _, row in profesores.iterrows()
    ]
    clases = [
        Clase(
            id=row['id'],
            nombre=row['nombre'],
            dia=row['dia'],
            horario=(row['inicio'], row['fin']),
            profesores=[
                int(idx)
                for idx in row['profesores_id'].split(',')
            ]
        )
        for _, row in clases.iterrows()
    ]
    return profesores, clases


Days: TypeAlias = int
Hours: TypeAlias = int
Minutes: TypeAlias = int
Seconds: TypeAlias = float


def elapsed_time(start: float, end: float) -> Tuple[Days, Hours, Minutes, Seconds]:
    seconds = end - start
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(int(minutes), 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


def print_elapsed_time(start: float, end: float) -> None:
    days, hours, minutes, seconds = elapsed_time(start, end)
    print(f'Elapsed Time: {days}D {hours}H {minutes}M {seconds}S')


def print_time(time_to_print: Optional[float] = None) -> float:
    if not time_to_print:
        time_to_print = time.time()
    str_time = datetime.datetime.fromtimestamp(time_to_print)
    print(f"[{str_time}]")
    return time_to_print


def timer(minutes: int) -> Callable[[], bool]:
    start: float = time.time()

    def still_time() -> bool:
        current_time: float = time.time()
        diff_time: float = current_time - start
        return minutes*60.0 > diff_time

    return still_time


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print_time(start)
        try:
            result = func(*args, **kwargs)
        except KeyboardInterrupt:
            end = print_time()
            print_elapsed_time(start, end)
            sys.exit("KeyboardInterrupt")
        except Exception as e:
            end = print_time()
            print_elapsed_time(start, end)
            raise e
        end = print_time()
        print_elapsed_time(start, end)
        return result
    return wrapper
