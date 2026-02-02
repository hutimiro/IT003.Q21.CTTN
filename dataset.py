import numpy as np
import pandas as pd

integers1 = np.random.randint(0, 1000001, 1000000)
integers2 = np.random.randint(0, 1000001, 1000000)
integers3 = np.random.randint(0, 1000001, 1000000)
integers4 = np.random.randint(0, 1000001, 1000000)
integers5 = np.random.randint(0, 1000001, 1000000)
real_numbers1 = np.random.rand(1000000) * 1000000
real_numbers2 = np.random.rand(1000000) * 1000000
real_numbers3 = np.random.rand(1000000) * 1000000
real_numbers4 = np.random.rand(1000000) * 1000000
real_numbers5 = np.random.rand(1000000) * 1000000

sorted_arr1 = np.sort(integers1)
sorted_arr2 = np.sort(integers2)[::-1]

df = pd.DataFrame({
    'Integer_Column_1': sorted_arr1,
    'Integer_Column_2': sorted_arr2,
    'Integer_Column_3': integers3,
    'Integer_Column_4': integers4,
    'Integer_Column_5': integers5,
    'Real_Number_Column_1': real_numbers1,
    'Real_Number_Column_2': real_numbers2,
    'Real_Number_Column_3': real_numbers3,
    'Real_Number_Column_4': real_numbers4,
    'Real_Number_Column_5': real_numbers5
})

df.to_csv('random_numbers.csv', index=False)

print("File saved as random_numbers.csv")
