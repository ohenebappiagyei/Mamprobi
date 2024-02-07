import pandas as pd
import random

# Read the Excel file
file_path = r'C:\Users\HP\Desktop\codes\Mamprobi\RUM_prince\RUM.csv'

# Read the Excel file
df = pd.read_excel(file_path)

# Filter rows where Modality is OPD in column 10
df_opd = df[df['Modality'].str.contains('OPD', case=False, na=False)]

# Keep only relevant columns
relevant_columns = ['Modality', 'Provisional Diagnosis', 'Principal Diagnosis', 'Additional Diagnosis']
df_opd_relevant = df_opd[relevant_columns]

# Randomly select 50 rows
random_selection = df_opd_relevant.sample(n=50, random_state=42)  # You can change the random_state for different selections

# Save the results to a new Excel file
output_file_path = 'cleaned_data.xlsx'
random_selection.to_excel(output_file_path, index=False)

print(f"Data has been cleaned and saved to {output_file_path}.")

