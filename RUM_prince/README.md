Using the RUM Data Cleaning Script
To effectively use the RUM data cleaning script, follow these steps:

Excel Sheet Requirements:

Save your Excel sheet downloaded from the LHIMS as "RUM" and ensure the format is ".csv".
Preparation of Excel Sheet:

Delete all rows before reaching the actual headings.
The first cell in the first column should be the one labeled as "Sr.No."

Excluding Specific Medicines:

If you have other medicines to exclude because they are used for OPD consultations but are considered chronic care medicines, edit the exclude_medicines array in the script.
"exclude_medicines = [
    "Nifedipine", "Metformin", "Amlodipine", "Atorvastatin", 
    "Tamsulosin", "Atenolol", "Losartan", "Soluble Aspirin", 
    "Bendroflumethiazide", "Clopidogrel"
]"
Run the Script:

Execute the script in your preferred Python environment.
bash
```python RUM.py```

The cleaned and sampled data will be saved as "RUM_final_data.xlsx" in Excel format.

For help on running it in a python environment you can reach me via email ohenebappiagyei.com
