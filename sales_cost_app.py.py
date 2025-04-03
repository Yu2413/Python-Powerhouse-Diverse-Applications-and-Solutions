import pandas as pd

def main():
    print("Welcome! This script calculates Sales and Costs for different periods.")
    print("Please enter the amounts when prompted.\n")

    # 1. Prompt user for input
    weekly_sales   = float(input("Enter total weekly sales: "))
    weekly_cost    = float(input("Enter total weekly cost: "))
    monthly_sales  = float(input("\nEnter total monthly sales: "))
    monthly_cost   = float(input("Enter total monthly cost: "))
    quarterly_sales = float(input("\nEnter total quarterly sales: "))
    quarterly_cost  = float(input("Enter total quarterly cost: "))
    yearly_sales   = float(input("\nEnter total yearly sales: "))
    yearly_cost    = float(input("Enter total yearly cost: "))

    # 2. Store in a DataFrame
    data = {
        'Period': ['Weekly', 'Monthly', 'Quarterly', 'Yearly'],
        'Sales': [
            weekly_sales,
            monthly_sales,
            quarterly_sales,
            yearly_sales
        ],
        'Cost': [
            weekly_cost,
            monthly_cost,
            quarterly_cost,
            yearly_cost
        ]
    }
    df = pd.DataFrame(data)

    # 3. Calculate Profit
    df['Profit'] = df['Sales'] - df['Cost']

    # 4. Print Summary
    print("\n--- Sales vs. Cost Summary ---")
    print(df.to_string(index=False))

    # 5. (Optional) Export to CSV/Excel
    # df.to_csv("sales_cost_summary.csv", index=False)

if __name__ == "__main__":
    main()
