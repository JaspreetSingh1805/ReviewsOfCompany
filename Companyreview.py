import pandas as pd

# Load the master CSV file
master_df = pd.read_csv('master_file.csv')

# Add a new column 'Company name' with value 'IBM' for all rows
master_df['Company name'] = 'IBM'

# Save the updated DataFrame back to the CSV
master_df.to_csv('master_file.csv', index=False)

print("Column 'Company name' added to master_file.csv with value 'IBM'.")
