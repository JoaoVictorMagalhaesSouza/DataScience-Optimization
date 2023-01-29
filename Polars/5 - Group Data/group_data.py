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
#%% Creating DFs
pandas_df = pd.DataFrame(columns=['age',
                            'preferred_language',
                            'graduation',
                            'salary',
                                'favorite_theme',
                                'occupation_area'],data=list(zip(age, preferred_language, graduation, salary, favorite_theme, occupation_area)))

polars_df = pl.DataFrame({'age': age,
                        'preferred_language': preferred_language,
                            'graduation': graduation,
                                'salary': salary,
                                    'favorite_theme': favorite_theme,
                                        'occupation_area': occupation_area})
#%% Grouping by Graduation, Occupation Area, Preferred Lang and Favorite Theme with Pandas
start = time.time()
pandas_grouped_df = pandas_df.groupby(['graduation', 'occupation_area', 'preferred_language', 'favorite_theme']).mean()
end = time.time()
time_to_group_pandas = end - start
print(f'Time to group with Pandas: {time_to_group_pandas:.2f} seconds')
#%% Grouping by Graduation, Occupation Area, Preferred Lang and Favorite Theme with Polars
start = time.time()
polars_grouped_df = polars_df.groupby(['graduation', 'occupation_area', 'preferred_language', 'favorite_theme']).agg(pl.mean('salary'))
end = time.time()
time_to_group_polars = end - start
print(f'Time to group with Polars: {time_to_group_polars:.2f} seconds')
#%% Plot the results
import matplotlib.pyplot as plt
plt.bar(['Pandas', 'Polars'], [time_to_group_pandas, time_to_group_polars])
plt.title('Time to group a DataFrame')
plt.ylabel('Time (s)')
plt.xlabel('Library')
plt.show()
#%%