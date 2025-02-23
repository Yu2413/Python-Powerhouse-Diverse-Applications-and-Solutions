import os
import pandas as pd

# Specify the folder containing the .txt files
folder_path = r"D:\names"  # Formatted folder path

# List to hold data from all .txt files
dataframes = []

# Loop through all .txt files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".txt"):  # Process only .txt files
        file_path = os.path.join(folder_path, file)
        try:
            # Read the .txt file into a DataFrame
            df = pd.read_csv(file_path, delimiter="\t", encoding="utf-8")  # Adjust delimiter and encoding if necessary
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

# Check if there are files to combine
if dataframes:
    # Combine all DataFrames into one
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Split the data into three parts
    total_rows = len(combined_df)
    part_size = total_rows // 3

    sheet1_df = combined_df.iloc[:part_size].copy()
    sheet1_df["Sheet"] = "Sheet1"

    sheet2_df = combined_df.iloc[part_size:2 * part_size].copy()
    sheet2_df["Sheet"] = "Sheet2"

    sheet3_df = combined_df.iloc[2 * part_size:].copy()
    sheet3_df["Sheet"] = "Sheet3"

    # Specify output Excel file path
    output_file = r"D:\Output\NewMicrosoftExcelWorksheet.xlsx"  # Formatted output path

    # Save the split DataFrames to separate sheets in the Excel file
    try:
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            sheet1_df.to_excel(writer, sheet_name="Sheet1", index=False)
            sheet2_df.to_excel(writer, sheet_name="Sheet2", index=False)
            sheet3_df.to_excel(writer, sheet_name="Sheet3", index=False)
        print(f"Combined data saved successfully in Excel format at: {output_file}")
    except Exception as e:
        print(f"Error saving the Excel file: {e}")
else:
    print("No valid .txt files found to combine.")