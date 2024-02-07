import pandas as pd
import random

# Read the Excel file
file_path = r'C:\Users\HP\Desktop\codes\Mamprobi\RUM_prince\RUM.csv'

# Read the Excel file
df = pd.read_excel(file_path)

# Delete the first 3 rows
# df = df.iloc[3:]

print(df.columns)

# Extract specific columns
columns_to_keep = ['Modality', 'Provisional Diagnosis','Principal Diagnosis', 'Additional Diagnosis', 'Medicine Prescribed', 'Medicine Dispensed']
df_cleaned = df[columns_to_keep]

# Save the cleaned data to a new file
cleaned_file_path = 'cleaned_RUM.xlsx'
df_cleaned.to_excel(cleaned_file_path, index=False)

# Extract data where 'Modality' column contains 'OPD'
opd_data = df[df['Modality'] == 'OPD']
opd_file_path = 'opd_data.xlsx'
opd_data.to_excel(opd_file_path, index=False)

# Randomly select 50 rows from Diagnosis
diagnosis_columns = ['Provisional Diagnosis', 'Principal Diagnosis', 'Additional Diagnosis']
random_diagnosis_data = pd.concat([df[col].sample(50, replace=True) for col in diagnosis_columns], axis=1)

# Save the randomly selected diagnosis data to a new file
random_diagnosis_file_path = 'RUM_final.xlsx'
random_diagnosis_data.to_excel(random_diagnosis_file_path, index=False)
