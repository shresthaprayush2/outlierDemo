# pip install pandas
# pip install scipy
# pip install seaborn
# pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from scipy.stats import zscore

# Setting up the template
sns.set_style('whitegrid')
sns.set_palette('deep')
# Replace with your data
data = pd.read_excel('TestData.xlsx',sheet_name='AllDetails',parse_dates=['Date'])

print(data.sample(10))

# Visualizing the data
sns.scatterplot(data,x='Date',y='Expense')
# Using this to format the axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.title("Daily Expenses")
plt.savefig('dailyexpense.png')
plt.show()

# Fixing the Nan Value, THIS IS IMPORTANT TO GET ZSCORE
data.fillna(0,inplace=True)
# Fix the outlier with Zscore
score = zscore(data['Expense'])
print(score)

data['Zscore'] = score
# Getting the values that are outliers > 3
outliers = data[data['Zscore'].abs() > 3]
print(outliers)

# Plotting the data with outliers
sns.scatterplot(data=data, x='Date', y='Expense', label='Normal')
sns.scatterplot(data=outliers, x='Date', y='Expense', color='red', label='Outliers')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.title("Daily Expenses with Outliers")
plt.legend()
plt.savefig('dailyExpenseWithOutlier.png')
plt.show()


# Visualizing the zscore with histogram
plt.figure(figsize=(10, 5))
sns.histplot(data['Zscore'], kde=True, bins=30)
plt.axvline(3, color='red', linestyle='--', label='Z = 3')
plt.axvline(-3, color='red', linestyle='--', label='Z = -3')
plt.title('Z-Score Distribution of Expenses')
plt.xlabel('Z-Score')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('zScore.png')
plt.show()
