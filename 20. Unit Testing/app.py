from typing import Union


def add_number(a: int, b: int, c: int) -> int:
    return a + b + c


def divide(
    dividend: Union[int, float], divisor: Union[int, float]
) -> Union[int, float]:
    if divisor == 0:
        raise ValueError("Can't Divide something with zero")
    return dividend / divisor


def multiply(*args: Union[int, float]) -> Union[int, float]:
    if len(args) == 0:
        raise ValueError("Atleast one value must be provided")
    ans: int = 1
    for value in args:
        ans *= value
    return ans
