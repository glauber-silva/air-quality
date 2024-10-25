import xarray as xr



class NetCDFDataLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_set = None
        self.data_frame = None

    def load(self):
        self.data_set = xr.open_dataset(self.file_path)
        self.to_dataframe()

    def to_dataframe(self):
        self.data_frame = self.data_set.to_dataframe()

    def read_head(self):
        print(self.data_frame.head(5))

# import xarray as xr
# import pandas as pd

# # Load the NetCDF file
# ds = xr.open_dataset('path_to_your_file.nc')

# # Convert to pandas DataFrame
# df = ds.to_dataframe()

# # Optionally, reset the index if needed
# df.reset_index(inplace=True)

# print(df.head())