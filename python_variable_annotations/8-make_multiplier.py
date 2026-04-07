from typing import Callable

multiplier: float

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_fn(value: float) -> float:
        return value * multiplier
    return multiplier_fn
