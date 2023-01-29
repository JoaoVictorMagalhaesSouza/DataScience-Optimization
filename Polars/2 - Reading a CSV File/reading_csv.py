#%%
import pandas as pd
import polars as pl
import time
import numpy as np

# %% Reading a CSV file with Pandas
pandas_times = []
for i in range(10):
    start = time.time()
    pandas_df = pd.read_csv('input_data.csv')
    end = time.time()
    total_time_pandas_read = end - start
    pandas_times.append(total_time_pandas_read)

average_pandas = np.mean(pandas_times)
print(f'Time to read a CSV file with Pandas: {average_pandas:.2f} seconds')
#%% Reading a CSV file with Polars
polars_times = []
for i in range(10):
    start = time.time()
    polars_df = pl.read_csv('input_data.csv')
    end = time.time()
    total_time_polars_read = end - start
    polars_times.append(total_time_polars_read)

average_polars = np.mean(polars_times)
print(f'Time to read a CSV file with Polars: {average_polars:.2f} seconds')
# %% Plot the results
import matplotlib.pyplot as plt
plt.bar(['Pandas', 'Polars'], [average_pandas, average_polars])
plt.title('Average time to read a CSV file')
plt.ylabel('Time (s)')
plt.xlabel('Library')
plt.show()
#%%