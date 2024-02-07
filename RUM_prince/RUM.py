import pandas as pd

# Read the Excel file
file_path = r'C:\Users\HP\Desktop\codes\Mamprobi\RUM_prince\RUM.csv'
df = pd.read_excel(file_path)

# Keep rows where 'Modality' column contains 'OPD'
df_opd = df[df['Modality'].str.contains('OPD', case=False, na=False)]

# Exclude rows where 'medicine prescribed' column contains specific values
exclude_medicines = [
    "Nifedipine %", "Metformin %", "Amlodipine %", "Atorvastatin %", 
    "Tamsulosin %", "Atenolol %", "Losartan %", "Soluble Aspirin %", 
    "Bendroflumethiazide %", "Clopidogrel %"
]
df_opd_sample = df_opd[~df_opd['Medicine Prescribed'].isin(exclude_medicines)]

# Select 50 random rows
df_opd_sample = df_opd_sample.sample(n=50, random_state=42)  # You can change the random_state if needed

# Save the cleaned and sampled data to a new file
output_file_path = 'cleaned_data_opd.xlsx'
df_opd_sample.to_excel(output_file_path, index=False)

print(f'Data has been cleaned and saved to {output_file_path}')

