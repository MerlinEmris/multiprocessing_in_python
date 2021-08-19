import multiprocessing as mp
# import math
import json
import time
# import os
import sys


def fib(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def parallel(san1: int, san2: int) -> float:
    pool = mp.Pool(processes=mp.cpu_count())
    a = time.time()
    results = [pool.map(fib, (x for x in range(san1-1, san2)))]
    b = time.time()
    print("parallel: "+str(results))
    print(f'parallel time:{b-a}')
    return b-a


def normal(san1: int, san2: int) -> float:
    result = []
    a = time.time()
    for x in range(san1-1, san2):
        result.append(fib(x))
    b = time.time()
    print("series: "+str(result))
    print(f'series time:{b-a}')
    return b-a


def resulter(san1: int, san2: int) -> tuple:
    b = parallel(san1, san2)
    a = normal(san1, san2)
    print(f'delta time (series/parallel):{a/b}')
    return (san1, san2, a, b, a/b)


def main():
    data_start = 0
    data_end = 0
    print(f"cpu core count:{mp.cpu_count()}")
    try:
        data_start = int(sys.argv[1])
        data_end = int(sys.argv[2])
        print(f"values are {data_start} - {data_end}")
    except:
        data_start = 10
        data_end = 16
        print("values are 10 - 16")
    data = []
    data.append(resulter(data_start, data_end))
    filename = 'result.json'
    with open(filename, 'a+') as fio:
        json.dump(data, fio)


if __name__ == '__main__':
    main()
