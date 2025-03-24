import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class LayoffBenefitAnalysis:
    def __init__(self, organization_name):
        self.organization_name = organization_name
        self.analysis_data = {}

    def input_layoff_details(self,
                             total_employees,
                             proposed_layoff_count,
                             avg_salary,
                             severance_package_percentage=0.2):
        """
        Capture key layoff details and financial implications
        """
        self.analysis_data['total_employees'] = total_employees
        self.analysis_data['proposed_layoff_count'] = proposed_layoff_count
        self.analysis_data['avg_salary'] = avg_salary
        self.analysis_data['severance_package'] = avg_salary * severance_package_percentage * proposed_layoff_count

    def calculate_financial_impact(self,
                                   annual_operational_savings,
                                   recruitment_cost_per_hire=5000):
        """
        Analyze financial implications of layoffs
        """
        layoff_count = self.analysis_data['proposed_layoff_count']
        severance_cost = self.analysis_data['severance_package']

        recruitment_costs = recruitment_cost_per_hire * layoff_count
        total_immediate_costs = severance_cost + recruitment_costs
        net_first_year_savings = annual_operational_savings - total_immediate_costs

        self.analysis_data.update({
            'severance_costs': severance_cost,
            'recruitment_costs': recruitment_costs,
            'total_immediate_costs': total_immediate_costs,
            'annual_operational_savings': annual_operational_savings,
            'net_first_year_savings': net_first_year_savings
        })

    def social_impact_assessment(self,
                                 community_dependency_score=0.5,
                                 alternative_job_market_score=0.7):
        """
        Assess broader social and ethical implications
        """
        layoff_percentage = (self.analysis_data['proposed_layoff_count'] /
                             self.analysis_data['total_employees']) * 100

        social_impact_score = (1 - community_dependency_score) * (1 - alternative_job_market_score)

        self.analysis_data.update({
            'layoff_percentage': layoff_percentage,
            'social_impact_score': social_impact_score
        })

    def generate_report(self):
        """
        Generate comprehensive layoff impact report
        """
        print(f"Layoff Benefit Analysis for {self.organization_name}")
        print("\nFinancial Analysis:")
        for key, value in self.analysis_data.items():
            if isinstance(value, (int, float)):
                print(f"{key.replace('_', ' ').title()}: ${value:,.2f}")

        # Optional: Visualization
        plt.figure(figsize=(10, 6))
        plt.bar(
            ['Severance Costs', 'Recruitment Costs', 'Operational Savings'],
            [
                self.analysis_data['severance_costs'],
                self.analysis_data['recruitment_costs'],
                self.analysis_data['annual_operational_savings']
            ]
        )
        plt.title('Financial Impact of Layoffs')
        plt.ylabel('Cost/Savings ($)')
        plt.show()


def main():
    # Example usage
    nonprofit_analysis = LayoffBenefitAnalysis("Community Support Organization")

    nonprofit_analysis.input_layoff_details(
        total_employees=100,
        proposed_layoff_count=20,
        avg_salary=50000
    )

    nonprofit_analysis.calculate_financial_impact(
        annual_operational_savings=500000
    )

    nonprofit_analysis.social_impact_assessment()

    nonprofit_analysis.generate_report()


if __name__ == "__main__":
    main()
