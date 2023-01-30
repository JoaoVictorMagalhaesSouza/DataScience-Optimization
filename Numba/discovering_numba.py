#%%
from numba import jit
import time
import numpy as np
#%% Creating a array of 10000000 elements

#%% Creating a function to sum all elements of the array
@jit(nopython=True)
def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum
#%% Testing the function
numba_times = []
for i in range(100):
    start = time.time()
    array = np.random.randint(0,1000,10000000)
    sum_array(array)
    end = time.time()
    numba_times.append(end - start)
print("Time for sum with Numba: ", np.mean(numba_times))
#%%
#%% Creating a function to sum all elements of the array

def sum_without_numba(array):
    sum = 0
    for i in array:
        sum += i
    return sum
#%% Testing the function
without_numba_times = []
for i in range(100):
    start = time.time()
    array = np.random.randint(0,1000,10000000)
    sum_without_numba(array)
    end = time.time()
    without_numba_times.append(end - start)
print("Time for sum without Numba: ", np.mean(without_numba_times))
#%%