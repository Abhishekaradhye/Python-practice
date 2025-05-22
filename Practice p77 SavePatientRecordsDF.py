"""You are building a basic backend simulation for a healthcare system. 
Write a Python program that reads patient records from a CSV file and stores them in a DataFrame. 
Each record contains patient_id, name, date_of_birth, contact_number, and optionally medical_history. 
Implement a function to add each patient's information into the main dataset."""

import pandas as pd

# Start with an empty DataFrame with all required columns
patient_records_df = pd.DataFrame(columns=[
    'patient_id', 'name', 'date_of_birth', 'contact_number', 'medical_history'  # ✅ Added medical_history
])

# Function to save one patient record
def save_patient_data(patient_id, name, date_of_birth, contact_number, medical_history="NA"):
    # ✅ Appending data as a new row instead of replacing columns
    global patient_records_df
    new_row = {
        'patient_id': patient_id,
        'name': name,
        'date_of_birth': date_of_birth,
        'contact_number': contact_number,
        'medical_history': medical_history  # ✅ Added to keep data complete
    }
    patient_records_df = pd.concat([patient_records_df, pd.DataFrame([new_row])], ignore_index=True)

# ✅ Corrected loop to iterate over rows using .iterrows()
data_df = pd.read_csv('data.csv')  # Assuming data.csv has correct columns

for _, row in data_df.iterrows():
    # ✅ Use row['colname'] instead of row[index]
    save_patient_data(
        row['patient_id'],
        row['name'],
        row['date_of_birth'],
        row['contact_number'],
        row.get('medical_history', 'NA')  # ✅ Optional field with default
    )

# ✅ Optional: print final DataFrame to check
print(patient_records_df)
