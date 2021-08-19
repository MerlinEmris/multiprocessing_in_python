# Multiprocessing In Python

Calculating Fibonachi sequence siries and parallel; time comparizon!

## Roadmap

<ol>
    <li><a href="#roadmap">Roadmap</a></li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#usage/examples">Usage/Examples</a>
    </li>
    <li><a href="#running-tests">Running Tests</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    
  </ol>

---

## Installation

requires python >=3.6

```bash
git clone https://github.com/MerlinEmris/multiprocessing_in_python.git
```

```bash
python multiproces\multiprocess.py
```

---

## Usage/Examples

App gets 2 variables from num to num2
Application calculates Fibonachi secuence siries as normal python app and in parallel where task is seperated between cpu cores.

```bash
python multiproces\multiprocess.py 12 22
```

---

```bash
python multiproces\multiprocess.py 1 40
```

```bash
cpu core count:16
values are 1 - 40
parallel: [[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025,
121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]]
parallel time:15.866930961608887
series: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
series time:36.89705181121826
delta time (series/parallel):2.325405707032644
```

---

## Running Tests

To run tests, run the following command

```bash
  python multiproces\test.py
```

## Acknowledgements

- [Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
- [Multiprocessing in Python](https://www.geeksforgeeks.org/multiprocessing-python-set-1/)
