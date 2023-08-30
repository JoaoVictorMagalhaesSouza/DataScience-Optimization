from abc import ABC, abstractmethod
import polars as pl

class DataAcquisition(ABC):
    def __init__(self, filename):
        self.data_source = filename
    
    @abstractmethod
    def get_data(self):
        pass

class DataAcquistionFactory():    
    def get_data(self, strategy: DataAcquisition):
        return strategy.get_data()

class DataAcquisitionCSV(DataAcquisition):
    def __init__(self, filename):
        super().__init__(filename)
    
    def get_data(self):
        return pl.read_csv(self.data_source)

class DataAcquisitionParquet(DataAcquisition):
    def __init__(self, filename):
        super().__init__(filename)
    
    def get_data(self):
        return pl.read_parquet(self.data_source)

class DataAcquisitionJSON(DataAcquisition):
    def __init__(self, filename):
        super().__init__(filename)
    
    def get_data(self):
        return pl.read_json(self.data_source)

class DataAcquisitionExcel(DataAcquisition):
    def __init__(self, filename):
        super().__init__(filename)
    
    def get_data(self):
        return pl.read_excel(self.data_source)
