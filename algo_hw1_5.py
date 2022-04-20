# Problem 5: Prime numbers
import time

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.10f microseconds."
              % (func.__qualname__, (time.time() - start_time)*1e6))
        return result
    return measure_time

@timeit
def list_primes(n):
    primes = [2]
    if n == 0:
        return [0]

    i = 3
    while len(primes) < n:
        counter = [(i % j) == 0 for j in range(2, i-1, 2)]
        if sum(counter) == 0:
            primes.append(i)
        i += 1
    return primes

print(list_primes(10))
