import pandas as pd
import zipcodes

# Read your CSV file containing ZIP codes (one per line)
df = pd.read_csv("C:/Users/Yu241/Desktop/my_zip_list_1.csv", header=None, names=["Zip"], dtype={"Zip": str})

# Function to look up the county for a given ZIP code
def lookup_county(zip_code):
    result = zipcodes.matching(zip_code)
    if result:
        return result[0].get("county", "Not Found")
    return "Not Found"

# Apply the lookup function to each ZIP code in the DataFrame
df["County"] = df["Zip"].apply(lookup_county)

# Save the DataFrame to an Excel file
output_file = "C:/Users/Yu241/Desktop/my_zip_list_with_counties_1.xlsx"
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")