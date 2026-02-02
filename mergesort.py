import numpy as np
import pandas as pd
import time
avgtime = 0
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        L = arr[:mid]        
        R = arr[mid:]

        merge_sort(L)        
        merge_sort(R)       

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    start_time = time.time()
    sorted_integers = merge_sort(df[col].tolist())
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using Mergesort: {(end_time - start_time) * 1000:.0f} ms") 
