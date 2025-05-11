import pandas as pd
import matplotlib.pyplot as plt
print("Pie Chart for Critical Inspection.")
print("Using Matplotlib Package")
#DataFrame
df = pd.read_csv('raw_data\\LMG_Inspection_Violations_of_Failed_Restaurants.csv')
#Setting Variables and failed criteria
filtered_df = df[df['score'] < 85]
colors={'No':'green', 'Yes':'red'}
value_counts = filtered_df['critical_yn'].value_counts()

#Plotting Pie Chart
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Critical Results')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()