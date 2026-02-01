import numpy as np
import pandas as pd
import time
avgtime = 0
df = pd.read_csv('random_numbers.csv')
for col in df.columns:
    print(f"Sorting column: {col}")
    start_time = time.time()
    sorted_integers = np.sort(df[col].to_numpy())
    end_time = time.time()
    avgtime = avgtime + (end_time - start_time)
    print(f"time taken to sort {col} using NumPy sort: {(end_time - start_time) * 1000:.0f} ms")
print(f"Average sorting time over all columns: {(avgtime / len(df.columns)) * 1000:.0f} ms")