import numpy as np
import pandas as pd
import time 
from numba import njit

avgtime = 0 

@njit
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

@njit
def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

heapsort(np.array([3, 1, 2], dtype=np.int64))

df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    data = df[col].to_numpy()
    start_time = time.time()
    sorted_integers = heapsort(data)
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using Heapsort: {(end_time - start_time) * 1000:.0f} ms")

avgtime = avgtime / len(df.columns)
print(f"average time taken to sort using Heapsort is: {avgtime * 1000:.0f} ms")
