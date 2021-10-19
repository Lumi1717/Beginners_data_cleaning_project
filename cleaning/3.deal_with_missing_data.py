# Imports
import pandas as pd
import numpy as np

data = pd.read_csv("sberbank.csv")

# There are 4 methods of dealing with missing data

# Solution #1: Drop the Observation
# This solution is credible if and only if we know that the information is not informative

for col in data.columns:
    missing = data[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print('Missing indicator: {}'.format(col))
        data['{}_ismissing'.format(col)] = missing

ismissing_cols = [col for col in data.columns if 'ismissing' in col]
data['num_missing'] = data[ismissing_cols].sum(axis=1)

indx_missing = data[data['num_missing'] > 35].index
data_over_missing = data.drop(indx_missing, axis=0)

# Solution #2: Drop the Feature
# Similar to the top only if the information is not informative
# In this example 'hospital_beds_raion' has 47% of missing data, we can drop this feature since it has no value to us

drop_feature = ['hospital_beds_raion']
drop_this = data.drop(drop_feature, axis=1)

# Solution #3: Input the Missing Data
# You can fill in the missing data my finding out the mean value of the feature

avg = data['life_sq'].median()
data['life_sq'] = data['life_sq'].fillna(avg)

# it is possible to fill in all missing values at once

data_num = data.select_dtypes(include=[np.number])
num_col = data_num.values

for col in num_col:
    missing = data[col].isnull()
    num_miss = np.sum(missing)

    if num_miss > 0 :
        print('Inputting missing value for: {}'.format(col))
        data['{}_ismissing'.format(col)] = missing

        avg = data[col].mediam()
        data[col] = data[col].fillna(avg)

# Solution #4: Replace Missing Values

# We can create a new category with values like 'missing' for a categorical features
# and '-999' for numerical features, this way we can keep the missing values

data['sub_area'] = data['sub_area'].fillna('Missing')

data['life_sq'] = data['life_sq'].fillna(-999)



