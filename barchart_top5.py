import pandas as pd
print("Horizontal Bar Chart Showing top 5 issues found.")
print("Using Matplotlib Package")
# Create DataFrame
data = pd.read_csv('raw_data\\LMG_Inspection_Violations_of_Failed_Restaurants.csv')
df = pd.DataFrame(data)

# Count occurrences of each value in 'Violation Description'
value_counts = df['ViolationDesc'].value_counts()

# Display the top 5 most frequent values
top_5 = value_counts.head(5)
top_5.head(5).plot(kind='barh')
plt.xlabel('Count of occurances')
plt.ylabel('Inspection Findings')
plt.title('Top 5 Issues Found')
plt.gca().invert_yaxis() 
plt.show()
#print(top_5)