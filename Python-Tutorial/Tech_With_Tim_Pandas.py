import pandas as pd
import openpyxl as xl
from pandasgui import show

orders1 = pd.read_csv(r"C:\VS Code Repo\Python\my_venv\CSV\orders.csv")

# show(orders1)
# orders1.info()
# Shows whole the DataFrame

# orders1.head()
# print(orders1.head())
# Shows the first 5 rows

# orders1.describe()
# print(orders1.describe())
# Gets statistical summary of numerical columns

# orders1.columns
# print(orders1.columns)
# Gets all column names

# orders1["Country"]
# print(orders1["Country"])
# Gets a single column: Country

# orders1[["Country", "Product"]]
# print(orders1[["Country", "Product"]])
# Gets two columns: Country and Product

# query1 = orders1.iloc[10]
# print(query1)
# Gets the 10th row, 9th index (index starts at 0)

# query2 = orders1.iloc[5]["Country"]
# print(query2)
# Gets the 6th row's, 5th index's country (index starts at 0)

# query3 = orders1[orders1["Product"] == "Laptop"]
# print(query3)
# Gets all rows where the Product is Laptop

# query4 = orders1[(orders1["Quantity"] > 10)]
# print(query4)
# Gets all rows where the Quantity is greater than 10

# query5 = orders1[(orders1["Country"].isin(["USA","UK","Germany"]))]
# print(query5)
# Gets all rows where the Country is USA, UK, or Germany

# query6 = orders1["Country"].unique()
# print(query6)
# Gets all unique values in the Country column

# Use drop to remove columns, and update to modify the DataFrame.

