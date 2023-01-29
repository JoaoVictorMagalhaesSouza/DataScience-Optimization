#%%
import pandas as pd
import numpy as np
import time
# %%
df = pd.DataFrame()
df['age'] = np.random.randint(18, 60, 1000000)
df['preferred_language'] = np.random.choice(['Python', 'R', 'Java', 'C++'], 1000000)
df['graduation'] = np.random.choice(['Computer Science','Engineering','Economy','Systems'], 1000000)
df['salary'] = np.random.randint(0, 10000, 1000000)
df['favorite_theme'] = np.random.choice(['Dark', 'Light'], 1000000)
df['occupation_area'] = np.random.choice(['Data Science', 'Web Apps', 'Mobile Apps', 'Software Engineering'], 1000000)
#%%
'''
    Challenge:
        - If salary > 5k, occupation area is Data Science and preferred lang is Python, is a good guy.
        - Else, is a bad guy.
'''
#%%
# Solution 1: By using apply
start = time.time()
def check_condition(row):
    if row['salary'] > 5000 and row['occupation_area'] == 'Data Science' and row['preferred_language'] == 'Python':
        return 'Good Guy'
    else:
        return 'Bad Guy'

df['good_guy?'] = df.apply(check_condition, axis=1)
end = time.time()
total_time_apply = end - start
# %% Solution 2: By using vectorization
start = time.time()
df['good_guy?'] = np.where((df['salary'] > 5000) & (df['occupation_area'] == 'Data Science') & (df['preferred_language'] == 'Python'), 'Good Guy', 'Bad Guy')
end = time.time()
total_time_vectorization = end - start
#%% Plotting times
import matplotlib.pyplot as plt
plt.bar(['Pandas Apply', 'Numpy Vectorization'], [total_time_apply, total_time_vectorization])
plt.title('Time to filter by Apply and Vectorization methods')
plt.ylabel('Time (s)')
plt.xlabel('Method')
plt.show()
#%%
