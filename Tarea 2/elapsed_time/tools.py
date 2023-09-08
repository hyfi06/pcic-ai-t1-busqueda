import datetime
import time
from typing import Tuple, TypeAlias, Optional


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
    print(f'Elapsed Time: {days}D{hours}H{minutes}M{seconds}S')


def print_time(time_to_print: Optional[float] = None) -> float:
    if not time_to_print:
        time_to_print = time.time()
    print(datetime.datetime.fromtimestamp(time_to_print))
    return time_to_print
