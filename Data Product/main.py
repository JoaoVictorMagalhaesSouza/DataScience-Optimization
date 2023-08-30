#%%
# Default imports
import polars as pl
import os

#Own imports
from classes import data_acquisition as da
from utils import (
    list_strategies as ls,
    create_fake_data as cfd,
)
#%% Setting the paths
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists('models'):
    os.makedirs('models')

DATA_PATH = 'data/'
MODELS_PATH = 'models/'

# %% List the strategies
da_strategies = ls.get_data_acquisition_strategies()
#%% Creating strategies
csv_strategy = da.DataAcquisitionCSV(DATA_PATH + 'fake_data.csv')
parquet_strategy = da.DataAcquisitionParquet(DATA_PATH + 'fake_data.parquet')
json_strategy = da.DataAcquisitionJSON(DATA_PATH + 'fake_data.json')
excel_strategy = da.DataAcquisitionExcel(DATA_PATH + 'fake_data.xlsx')
#%% Creating the factory
factory = da.DataAcquistionFactory()

csv_data = factory.get_data(csv_strategy)
parquet_data = factory.get_data(parquet_strategy)
json_data = factory.get_data(json_strategy)
excel_data = factory.get_data(excel_strategy)

# %%
