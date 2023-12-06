import pandas as pd

# Reading an Excel file
file_path = r'C:\Users\Yu241\OneDrive\Documents\Microsoft-365-Mastery-Integrating-and-Optimizing-Business-Solutions-Yu2413-Named-Method-Files\COUNTIFS_Excel_Analysis.xlsx'
df = pd.read_excel(file_path)

# Define the value to compare
comparison_value = "a"  # Replace 'a' with the actual value you want to compare

# Define the operator: '==' for equal, '>' for greater than
operator = '=='

# Perform operations based on the selected operator
if operator == '==':
    filtered_df = df[df['Q10'] == comparison_value]
elif operator == '>':
    filtered_df = df[df['Q10'] > comparison_value]

# Write to a new Excel file
output_file = 'processed_file.xlsx'
filtered_df.to_excel(output_file, index=False)
