import pandas as pd
import zipcodes

# Read the CSV file into a DataFrame
input_file = "C:/Users/Yu241/Desktop/my_zip_list_fis.csv"
df = pd.read_csv(input_file, header=0, names=["County", "Zip"], dtype={"Zip": str})

# Function to look up the state for a given ZIP code
def lookup_state(zip_code):
    result = zipcodes.matching(zip_code)
    if result:
        return result[0].get("state", "Not Found")
    return "Not Found"

# Apply the lookup function to each ZIP code in the DataFrame
df["State"] = df["Zip"].apply(lookup_state)

# Save the updated DataFrame to a new CSV file
output_csv_file = "C:/Users/Yu241/Desktop/my_zip_list_fis_output.csv"
df.to_csv(output_csv_file, index=False)

# Save the updated DataFrame to a new Excel file
output_excel_file = "C:/Users/Yu241/Desktop/my_zip_list_fis.xlsx"
df.to_excel(output_excel_file, index=False)

print(f"Data saved to {output_csv_file} and {output_excel_file}")