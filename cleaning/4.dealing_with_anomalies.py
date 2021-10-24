# Imports
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("sberbank.csv")


# How to find anomalies in the data

# Technique #1: Histogram/Box Plot
# To find numeric anomalies we use histograms

data['life_sq'].hist(bins=100)
plt.show()

# From the outcome we can see how skewed the data is
# We will sue a boxplot to clarify the anomaly

data.boxplot(column=['life_sq'])
plt.show()

# Technique #2: Descriptive Statistics
print(data['life_sq'].describe())

# To find all of the statistics of every column.
print(data.describe().T)

# From the solutdion we can see that the anomaly is the value 7478.
# Why ? because 75% of data is only 43


# Technique #3: Bar Chart
# Bar char is only used with categorical features

data['ecology'].value_counts().plot.bar()
plt.show()

# This outcome shows how even the feature is
