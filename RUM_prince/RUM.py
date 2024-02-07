from pathlib import Path
import pandas as pd

# Path to project
BASE_DIR = Path(__file__).resolve().parent 

# Specify the relative path to the CSV file
file_path = BASE_DIR/'RUM.csv'

# Read the Excel file
df = pd.read_excel(file_path)

# Keep rows where 'Modality' column contains 'OPD'
df_opd = df[df['Modality'].str.contains('OPD', case=False, na=False)]

# Exclude rows where 'medicine prescribed' column contains specific values
exclude_medicines = [
    "Nifedipine", "Metformin", "Amlodipine", "Atorvastatin", 
    "Tamsulosin", "Atenolol", "Losartan", "Soluble Aspirin", 
    "Bendroflumethiazide", "Clopidogrel", "Labetalol"
]

# Create a regex pattern for matching any part of the string
pattern = '|'.join(exclude_medicines)

# Use str.contains with the regex pattern
df_opd_sample = df_opd[~df_opd['Medicine Prescribed'].str.contains(pattern, case=False, na=False)]

# Select 50 random rows
df_opd_sample = df_opd_sample.sample(n=50, random_state=42)

# Save the cleaned and sampled data to a new file
output_file_path = BASE_DIR / 'RUM_final_data.xlsx'
df_opd_sample.to_excel(output_file_path, index=False)

print(f'Data has been cleaned and saved to {output_file_path}')

