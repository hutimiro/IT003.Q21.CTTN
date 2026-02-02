import numpy as np
import pandas as pd
import time 

avgtime = 0 

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
    return arr
def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2    # right = 2*i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        heapify(arr, n, largest)
df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    start_time = time.time()
    sorted_integers = heapsort(df[col].tolist())
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using Heapsort: {(end_time - start_time) * 1000:.0f} ms")

avgtime = avgtime / len(df.columns)
print(f"average time taken to sort using Heapsort is: {avgtime * 1000:.0f} ms")
