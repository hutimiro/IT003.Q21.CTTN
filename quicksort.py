import numpy as np
import pandas as pd
import time 

avgtime = 0

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    start_time = time.time()
    sorted_integers = quicksort(df[col].tolist())
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using Quicksort: {(end_time - start_time) * 1000:.0f} ms")

avgtime = avgtime / len(df.columns)
print(f"average time taken to sort using Quicksort is: {avgtime * 1000:.0f} ms")