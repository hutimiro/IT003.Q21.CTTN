import numpy as np
import pandas as pd
import time 
from numba import njit

avgtime = 0

@njit
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = arr[arr < pivot]
    middle = arr[arr == pivot]
    right = arr[arr > pivot]
    
    l_sorted = quicksort(left)
    r_sorted = quicksort(right)
    
    res = np.empty(len(l_sorted) + len(middle) + len(r_sorted), dtype=arr.dtype)
    res[:len(l_sorted)] = l_sorted
    res[len(l_sorted):len(l_sorted)+len(middle)] = middle
    res[len(l_sorted)+len(middle):] = r_sorted
    return res

df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    data = df[col].to_numpy()
    if col == df.columns[0]:
        _ = quicksort(data.copy())
        
    start_time = time.time()
    sorted_integers = quicksort(data)
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using Quicksort: {(end_time - start_time) * 1000:.0f} ms")

avgtime = avgtime / len(df.columns)
print(f"average time taken to sort using Quicksort is: {avgtime * 1000:.0f} ms")
