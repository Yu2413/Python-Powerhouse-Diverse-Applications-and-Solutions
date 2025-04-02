class RestaurantROI:
    def __init__(self):
        # Initial investment costs
        self.initial_investment = 0

        # Monthly financial metrics
        self.monthly_revenue = 0
        self.monthly_expenses = 0

        # Additional financial parameters
        self.annual_growth_rate = 0
        self.investment_period = 0

    def set_initial_investment(self, amount):
        """Set the total initial investment cost"""
        self.initial_investment = amount

    def set_monthly_revenue(self, revenue):
        """Set the monthly revenue"""
        self.monthly_revenue = revenue

    def set_monthly_expenses(self, expenses):
        """Set the monthly operating expenses"""
        self.monthly_expenses = expenses

    def set_annual_growth_rate(self, rate):
        """Set the annual revenue growth rate"""
        self.annual_growth_rate = rate

    def set_investment_period(self, years):
        """Set the investment analysis period"""
        self.investment_period = years

    def calculate_total_revenue(self):
        """Calculate cumulative revenue over the investment period"""
        total_revenue = 0
        current_monthly_revenue = self.monthly_revenue

        for year in range(self.investment_period):
            # Calculate annual revenue
            annual_revenue = current_monthly_revenue * 12
            total_revenue += annual_revenue

            # Increase revenue based on growth rate
            current_monthly_revenue *= (1 + self.annual_growth_rate)

        return total_revenue

    def calculate_total_expenses(self):
        """Calculate cumulative expenses over the investment period"""
        total_expenses = 0
        current_monthly_expenses = self.monthly_expenses

        for year in range(self.investment_period):
            # Calculate annual expenses
            annual_expenses = current_monthly_expenses * 12
            total_expenses += annual_expenses

            # Potential expense increase (optional)
            current_monthly_expenses *= 1.03  # 3% annual expense increase

        return total_expenses

    def calculate_roi(self):
        """Calculate Return on Investment (ROI)"""
        total_revenue = self.calculate_total_revenue()
        total_expenses = self.calculate_total_expenses()

        # Net profit calculation
        net_profit = total_revenue - total_expenses - self.initial_investment

        # ROI calculation
        roi = (net_profit / self.initial_investment) * 100

        return {
            'Total Revenue': total_revenue,
            'Total Expenses': total_expenses,
            'Net Profit': net_profit,
            'ROI (%)': roi
        }


def main():
    # Create restaurant ROI analysis
    restaurant = RestaurantROI()

    # Example inputs (replace with actual data)
    restaurant.set_initial_investment(250000)  # Initial startup costs
    restaurant.set_monthly_revenue(50000)  # Monthly revenue
    restaurant.set_monthly_expenses(40000)  # Monthly expenses
    restaurant.set_annual_growth_rate(0.05)  # 5% annual revenue growth
    restaurant.set_investment_period(5)  # 5-year analysis period

    # Calculate and display ROI
    results = restaurant.calculate_roi()

    print("Restaurant ROI Analysis:")
    for key, value in results.items():
        print(f"{key}: ${value:,.2f}")


if __name__ == "__main__":
    main()