
import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Час виконання функції: {execution_time:.3f} секунди")

        return result

    return wrapper


@measure_time
def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total


result = calculate_sum(1_000_000)
print(f"Сума чисел: {result}")
