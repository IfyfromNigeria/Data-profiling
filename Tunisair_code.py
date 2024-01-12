import pandas as pd
from ydata_profiling import ProfileReport
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\Users\\HP\\Downloads\\Tunisair_flights_dataset.csv', encoding = 'utf-8')

info = df.info()
head = df.head()
print(info)
print(head)

# Checking for missing values
missing = df.isnull().sum()
print(missing) #there are no missing values in this dataset

# Summary statistics of the dataset
desc_stat = df.describe()
print(desc_stat)

#Profile report
# profile = ProfileReport(df, title="data", html={'style': {'full_width': True}})
# output_file_path = 'C:\\Users\\HP\\Documents\\Tunis_Air_Flights_Analysis.html'
# profile.to_file(output_file=output_file_path)

IQR_threshhold = df[df['Arrival delay']>43]

print('\033[4mSUMMARY OF THE DATA FROM THE PROFILE REPORT\033[0m')
print('''From the report, there are 9 columns and 107,833 rows.\nInside these 9 columns,
2 are datetime(continuous) features, 5 are text features,
1 categorical feature and 1 numerical feature.
There are no missing values and no duplicate rows.
The report also shows that there is little or no correlation between the variables.
Using the Interquartile Range(IQR) method to search for outliers,
it appeared that the data had some outliers''')

sns.boxplot(x=df['Arrival delay'])


sns.violinplot(x=df['Arrival delay'])
plt.show()