#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt


#DataFrame
print("Stem Plot showing Zipcode and score.")
print("Using Matplotlib and IPython Packages")
data_df = pd.read_csv('raw_data\\characters.csv')

# Function to get unique values from a column
def get_unique_values(data_df, column):
    return data_df[column].unique().tolist()


#unique_values = get_unique_values(data_df, column='gender')
gender_code = 'sex'
unique_values = get_unique_values(data_df, gender_code)

# Group by 'Gender'
grouped = data_df.groupby('sex')
male_SW = data_df.query("sex == 'Male'")
female_SW = data_df.query("sex == 'Fmale'")
# Create the stem plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed

# Plot each column with a label for the legend
plt.stem(data_df.index, data_df['species'], markerfmt='ro', label='Species')

# Add labels and title
plt.ylabel('Species')
plt.title('Species of Characters in the Star Wars Movies.')

# Horizontal line
plt.grid(color='black', axis='y')

# Add legend
plt.legend()
plt.gca().invert_yaxis() 

plt.show()
