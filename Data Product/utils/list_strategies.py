from classes import data_acquisition as da

def get_data_acquisition_strategies() -> dict:
    return {
        'csv': da.DataAcquisitionCSV,
        'parquet': da.DataAcquisitionParquet,
        'json': da.DataAcquisitionJSON,
        'excel': da.DataAcquisitionExcel
    }