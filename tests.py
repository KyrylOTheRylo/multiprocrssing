import time
from functools import wraps

c1 = 0.0015475749969482422


def fib_memory(function):
    cache = {}

    @wraps(function)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            cache[args] = function(*args)
            return cache[args]

    return wrapper


@fib_memory
def fibonacci(n: int):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


a = time.time()
print(fibonacci(500))
b = time.time()
print(b - a,  sep="\n")
