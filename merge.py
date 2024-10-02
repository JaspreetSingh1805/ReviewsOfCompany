# import pandas as pd

# # Load the master CSV file
# master_df = pd.read_csv('master_file.csv')

# # Add the 'Company name' column if it doesn't exist already
# if 'Company name' not in master_df.columns:
#     master_df['Company name'] = 'IBM'

# # Move the 'Company name' column to the first position
# cols = ['Company name'] + [col for col in master_df.columns if col != 'Company name']
# master_df = master_df[cols]

# # Save the updated DataFrame back to the CSV
# master_df.to_csv('master_file1.csv', index=False)

# print("Moved 'Company name' column to the first position in master_file.csv.")
# import csv

# csv_filename = "synopsys.csv"
# new_rating = "4.6"
# company_name = "Synopsys"

# # Create a list to store the updated rows
# updated_rows = []

# # Open the existing CSV file
# with open(csv_filename, mode='r', newline='', encoding='utf-8-sig') as file:
#     reader = csv.reader(file)
    
#     # Read the header
#     header = next(reader)
    
#     # Ensure the header matches expected columns
#     if header[2] != "Overall Company Rating":
#         raise ValueError("The third column is not 'Overall Company Rating'. Check the CSV structure.")
    
#     # Modify the header to add "Company" as the first column
#     if header[0] != "Company":
#         header.insert(0, "Company")
    
#     # Append the modified header to the updated rows
#     updated_rows.append(header)
    
#     # Iterate through the remaining rows and add company name to the first column and new rating to the third column
#     for row in reader:
#         row[2] = new_rating  # Update the third column with the new rating
        
#         # Add the company name to the first column
#         if row[0] != company_name:
#             row.insert(0, company_name)
        
#         updated_rows.append(row)

# # Write the updated rows back to the CSV
# with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file)
#     writer.writerows(updated_rows)

# print(f"Successfully updated 'Overall Company Rating' to {new_rating} and added company name '{company_name}' in {csv_filename}.")
import pandas as pd
import os
import pdb
pdb.set_trace()
# List of all your CSV files
csv_files = [
    "Accenture_file.csv", "Capgemini_file.csv", "EY_file.csv", "Google_file.csv", 
    "IBM.csv", "Oracle_file.csv", "Siemens_file.csv", "synopsys.csv", 
    "Techmahindra_file.csv", "Microsoft_file.csv"
]

# Create an empty list to store dataframes
df_list = []

# Loop through each CSV file and read it into a pandas dataframe
for file in csv_files:
    if os.path.exists(file):  # Check if the file exists
        df = pd.read_csv(file)
        df_list.append(df)
    else:
        print(f"File not found: {file}")

# Concatenate all dataframes into one master dataframe
master_df = pd.concat(df_list, ignore_index=True)

# Save the master dataframe to a CSV file
master_csv_filename = "master_csv.csv"
master_df.to_csv(master_csv_filename, index=False, encoding='utf-8-sig')

print(f"Successfully merged all CSV files into {master_csv_filename}.")

