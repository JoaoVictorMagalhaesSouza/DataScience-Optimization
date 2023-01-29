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
#%% Filtering with Vectorization with Pandas
'''
    Conditions:
    - Age > 30
    - Salary > 5000
    - Preferred language is Python
    - Favorite theme is Light
    - Graduation is Computer Science
'''
start = time.time()
pandas_filtered_df = pandas_df[(pandas_df['age'] > 30) & (pandas_df['salary'] > 5000) & (pandas_df['preferred_language'] == 'Python') & (pandas_df['favorite_theme'] == 'Light') & (pandas_df['graduation'] == 'Computer Science')]
end = time.time()
time_to_filter_pandas = end - start
print(f'Time to filter with Pandas: {time_to_filter_pandas:.2f} seconds')
#%% Filtering with Vectorization with Polars
start = time.time()
polars_filtered_df = polars_df.filter((polars_df['age'] > 30) & (polars_df['salary'] > 5000) & (polars_df['preferred_language'] == 'Python') & (polars_df['favorite_theme'] == 'Light') & (polars_df['graduation'] == 'Computer Science'))
end = time.time()
time_to_filter_polars = end - start
print(f'Time to filter with Polars: {time_to_filter_polars:.2f} seconds')
#%% Plot the results
import matplotlib.pyplot as plt
plt.bar(['Pandas', 'Polars'], [time_to_filter_pandas, time_to_filter_polars])
plt.title('Time to filter a DataFrame')
plt.ylabel('Time (s)')
plt.xlabel('Library')
plt.show()
#%%
