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
    print(f'parallel wagt {b-a}')
    return b-a


def normal(san1: int, san2: int) -> float:
    result = []
    a = time.time()
    for x in range(san1-1, san2):
        result.append(fib(x))
    b = time.time()
    print("adaty: "+str(result))
    print(f'adaty wagt {b-a}')
    return b-a


def resulter(san1: int, san2: int) -> tuple:
    b = parallel(san1, san2)
    a = normal(san1, san2)
    print(f'adatynyň parallel wagt gatnaşygy:{a/b}')
    return (san1, san2, a, b, a/b)


def main():
    data_start = 0
    data_end = 0
    try:
        data_start = int(sys.argv[1])
        data_end = int(sys.argv[2])
        print(f"value set to {data_start} - {data_end}")
    except:
        data_start = 10
        data_end = 16
        print("value set to 10 - 16")
    data = []
    data.append(resulter(data_start, data_end))
    filename = 'result.json'
    with open(filename, 'a+') as fio:
        json.dump(data, fio)


if __name__ == '__main__':
    main()
