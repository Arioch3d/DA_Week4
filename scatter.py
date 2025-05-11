import pandas as pd
import matplotlib.pyplot as plt

penguin_data = pd.read_csv('raw_data/penguins.csv')

null_values_avg_df = penguin_data.copy()

null_values_avg_df['bill_length_mm'] = null_values_avg_df[['bill_length_mm']].fillna(null_values_avg_df[['bill_length_mm']].mean())
null_values_avg_df['bill_depth_mm'] = null_values_avg_df[['bill_depth_mm']].fillna(null_values_avg_df[['bill_depth_mm']].mean())
null_values_avg_df['flipper_length_mm'] = null_values_avg_df[['flipper_length_mm']].fillna(null_values_avg_df[['flipper_length_mm']].mean())
null_values_avg_df['body_mass_g'] = null_values_avg_df[['body_mass_g']].fillna(null_values_avg_df[['body_mass_g']].mean())
null_values_avg_df['sex'] = null_values_avg_df[['sex']].fillna('UNK')



penguins_df = null_values_avg_df.copy()

Chinstrap_df = penguins_df[penguins_df['species'] == 'Chinstrap']
Chinstrap_df 

species_flipper_average = penguin_data.groupby('species')['body_mass_g'].mean().reset_index().round(0)

species_flipper_average
male_Chinstrap = Chinstrap_df.query("sex == 'MALE'")
female_Chinstrap = Chinstrap_df.query("sex == 'FEMALE'")

plt.scatter(female_Chinstrap['flipper_length_mm'],female_Chinstrap['bill_length_mm'],label='Female', color='green')
plt.scatter(male_Chinstrap['flipper_length_mm'],male_Chinstrap['bill_length_mm'],label='Male', color='red')

plt.legend()