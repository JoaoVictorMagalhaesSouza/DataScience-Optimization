#%%
import polars as pl
import pandas as pd
import numpy as np
import time
# %%
samples = 10000000
age = np.random.randint(18, 60, samples)
preferred_language = np.random.choice(['Python', 'R', 'Java', 'C++'], samples)
graduation = np.random.choice(['Computer Science','Engineering','Economy','Systems'], samples)
salary = np.random.randint(0, 10000, samples)
favorite_theme = np.random.choice(['Dark', 'Light'], samples)
occupation_area = np.random.choice(['Data Science', 'Web Apps', 'Mobile Apps', 'Software Engineering'], samples)
#%% Creating a DataFrame with Pandas
pandas_times = []
for i in range(10):
    start = time.time()
    pandas_df = pd.DataFrame(columns=['age',
                            'preferred_language',
                            'graduation',
                            'salary',
                                'favorite_theme',
                                'occupation_area'],data=list(zip(age, preferred_language, graduation, salary, favorite_theme, occupation_area)))
    end = time.time()
    total_time_pandas = end - start
    pandas_times.append(total_time_pandas)
#Average time
print(f'Time to create a DataFrame with Pandas: {np.mean(pandas_times):.2f} seconds')
#%% Creating a DataFrame with Polars
polars_times = []
for i in range(10):
    start = time.time()
    polars_df = pl.DataFrame({'age': age,
                        'preferred_language': preferred_language,
                            'graduation': graduation,
                                'salary': salary,
                                    'favorite_theme': favorite_theme,
                                        'occupation_area': occupation_area})
    end = time.time()
    total_time_polars = end - start 

    polars_times.append(total_time_polars)

#Average time
print(f'Time to create a DataFrame with Polars: {np.mean(polars_times):.2f} seconds')


#%% Plot the results
import matplotlib.pyplot as plt
plt.bar(['Pandas', 'Polars'], [total_time_pandas, total_time_polars])
plt.title('Average time to create a DataFrame')
plt.ylabel('Time (s)')
plt.xlabel('Library')
plt.show()


#%%
