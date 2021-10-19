# Imports
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt


data = pd.read_csv("sberbank.csv")

# Taking only the first 30 columns to visualize the dataset
cols = data.columns[:30]

# # This section will print the the first 30 columns and the mean percentage of missing data
for col in data.columns:
    per_missing = np.mean(data[col].isnull())
    print('{} - {}%'.format(col, round(per_missing * 100)))

# This section will a show a heatmap of the missing data
palette = ['#f4d03f', '#0a2c52'] # the blue is missing data and the yellow is not the missing data
sns.heatmap(data[cols].isnull(), cmap=sns.color_palette(palette))
plt.show()


# View data loss that is greater than 25% because any loss of that magnitude tends to affect the outcome
over_flow = []
over_col = []
for col in data.columns:
    num = np.mean(data[col].isnull())
    over_missing = round(num * 100)

    if over_missing > 25:
        print('{} - {}%'.format(col, over_missing))
        over_flow.append(over_missing)
        over_col.append(col)

# Scatter chart representing the missing data over 25%
plt.title('Columns of Missing data over 25%')
plt.xlabel('Percentage of missing data')
plt.scatter(over_flow, over_col)
plt.show()

# Visualize the values with no mussing values
for col in data.columns:
    missing = data[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print('Missing indicator: {}'.format(col))
        data['{}_ismissing'.format(col)] = missing

ismissing_cols = [col for col in data.columns if 'ismissing' in col]
data['num_missing'] = data[ismissing_cols].sum(axis=1)
data['num_missing'].value_counts().reset_index().sort_values(by='index').plot.bar(x='index', y='num_missing')
plt.show()