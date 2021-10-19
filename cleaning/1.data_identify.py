# Imports
import pandas as pd
import numpy as np
data = pd.read_csv("sberbank.csv")

# View the datatype and the shape of the dataset
print(data.shape)
print(data.dtypes)

# Show the numerical columns
data_numeric = data.select_dtypes(include=[np.number])
numeric_cols = data_numeric.columns.values
print("Numerical Columns: ",numeric_cols)

# SHow the non numercial columns
data_non_numeric = data.select_dtypes(exclude=[np.number])
non_numeric_cols = data_non_numeric.columns.values
print("Non-Numerical Columns:",non_numeric_cols)