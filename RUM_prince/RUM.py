import pandas as pd

# Read the Excel file
file_path = 'your_file_path.xlsx'
df = pd.read_excel(file_path)

# Keep rows where 'Modality' column contains 'OPD'
df_opd = df[df['Modality'].str.contains('OPD', case=False, na=False)]

# Select 50 random rows
df_opd_sample = df_opd.sample(n=50, random_state=42)  # You can change the random_state if needed

# Save the cleaned and sampled data to a new file
output_file_path = 'cleaned_data_opd.xlsx'
df_opd_sample.to_excel(output_file_path, index=False)

print(f'Data has been cleaned and saved to {output_file_path}')

