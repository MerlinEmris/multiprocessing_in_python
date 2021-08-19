import multiprocessing as mp
import json
import time
import sys


def fib(n: int) -> int:
    """
        Calculate n'th number in Fibonachi secuence
        @return n'th nubmer
    """
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def parallel(san1: int, san2: int) -> list:
    """
        Calculates Fibonachi secuense between san1 and san2 parallel
        @return list of time taken by calculation, results
    """
    pool = mp.Pool(processes=mp.cpu_count())
    a: float = time.time()
    results = [pool.map(fib, (x for x in range(san1-1, san2)))]
    b: float = time.time()
    print("parallel: "+str(results))
    print(f'parallel time:{b-a}')
    return [b-a, results]


def normal(san1: int, san2: int) -> list:
    """
        Calculates Fibonachi secuense between san1 and san2 series
        @return time taken by calculation
    """
    results = []
    a: float = time.time()
    for x in range(san1-1, san2):
        results.append(fib(x))
    b: float = time.time()
    print("series: "+str(results))
    print(f'series time:{b-a}')
    return [b-a, results]


def resulter(san1: int, san2: int) -> tuple:
    """
        Makes calculations siries and parallel
        @return san1, san2, series calc time, parallel calc time, series/parallel
    """
    b: float = parallel(san1, san2)[0]
    a: float = normal(san1, san2)[0]
    print(f'delta time (series/parallel):{a/b}')
    return (san1, san2, a, b, a/b)


def main():
    data_start: int = 0
    data_end: int = 0
    print(f"cpu core count:{mp.cpu_count()}")
    try:
        data_start = int(sys.argv[1])
        data_end = int(sys.argv[2])
        print(f"values are {data_start} - {data_end}")
    except:
        data_start = 10
        data_end = 16
        print("values are 10 - 16")
    return resulter(data_start, data_end)


if __name__ == '__main__':
    main()
