# Imports
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

data = pd.read_csv("sberbank.csv")

# How to find unnecessary data types
# Features can be uninformative by having too many repetitive values

# Unnecessary type #1: Uninformative / Repetitive
num_row = len(data.index)
low_info_cols = []

for cols in data.columns:
    cnt = data[cols].value_counts(dropna=False)
    top_pct = (cnt/num_row).iloc[0]

    if top_pct > 0.95:
        low_info_cols.append(cols)
        print('{0}: {1:.5f}%'.format(cols, (top_pct*100)))
        print(cnt)

# Unnecessary type #2: Irrelevant
# If the feature does not serve any purpose to our question then we can delete the entire feature

# Unnecessary type #3: Duplicates
# Duplicates happen when copies of the same observation exist

# Duplicates type #1: All Features based
# Delete the id column because they are unique
find = data['id']
dupes = data.drop('id', axis=1).drop_duplicates()

print(data.shape)
print(dupes.shape)

# To find the dupes in each feature
for col in data.columns:
    dupes = data.duplicated([col])
    n_dupes = np.sum(dupes)

    print('{} has {} dupes'.format(col, n_dupes))

# Duplicates type #2: Key Features based
# You can remove duplicates based on a set of unique identifiers
# This method helps you find redundancy in specific a set of features

key = ['timestamp', 'full_sq', 'life_sq', 'floor', 'build_year', 'num_room', 'price_doc']
a = data.fillna(-999).groupby(key)['id'].count().sort_values(ascending=False).head(20)
de_dupe = data.drop_duplicates(subset= key)

print(data.shape)
print(de_dupe.shape)

