import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Sample DataFrame
print("Bar Chart Showing Top 5 Zip Codes")
print("Using Matplotlib and IPython Packages")
data_df = pd.read_csv('raw_data\\LMG_Inspection_Violations_of_Failed_Restaurants.csv')
import pandas as pd

# Sample DataFrame
df = pd.read_csv('raw_data\\LMG_Inspection_Violations_of_Failed_Restaurants.csv')
filtered_df = df[df['score'] < 85]
#unique_count = df['critical_yn'].value_counts()
#print(filtered_df)
colors={'No':'green', 'Yes':'red'}
value_counts = filtered_df['critical_yn'].value_counts()
plt.bar(x=value_counts.index, height=value_counts.values,color=[colors[i] for i in value_counts.index])
plt.xlabel(f'Categories {value_counts}')
plt.ylabel('Number of Critical Inspections')
plt.title('Critical Failed Inspections \n Using Matplotlib Data Package')
plt.show()