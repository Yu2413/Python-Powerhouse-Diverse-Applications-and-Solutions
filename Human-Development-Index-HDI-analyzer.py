#!/usr/bin/env python3
"""
HDI Analyzer Script

This script calculates the Human Development Index (HDI) for a country
based on key indicators:
- Life expectancy,
- Mean years of schooling,
- Expected years of schooling, and
- GNI per capita (in international dollars).

It computes three sub-indices as per the UNDP methodology and then derives
the overall HDI using the geometric mean of these indices. Finally, it classifies
the country based on the computed HDI value.
"""

import math


def calculate_life_index(life_expectancy: float, min_life: float = 20, max_life: float = 85) -> float:
    """
    Calculate the Life Expectancy Index.
    """
    index = (life_expectancy - min_life) / (max_life - min_life)
    # Ensuring the index stays within the [0, 1] range.
    return max(0, min(index, 1))


def calculate_education_index(mean_years: float, expected_years: float,
                              max_mean_years: float = 15, max_expected_years: float = 18) -> float:
    """
    Calculate the Education Index as the average of the mean years of schooling index and
    the expected years of schooling index.
    """
    mean_years_index = mean_years / max_mean_years
    expected_years_index = expected_years / max_expected_years
    education_index = (mean_years_index + expected_years_index) / 2
    # Ensuring the index is within the [0, 1] range.
    return max(0, min(education_index, 1))


def calculate_income_index(income: float, min_income: float = 100, max_income: float = 75000) -> float:
    """
    Calculate the Income Index using the natural logarithm transformation.
    """
    # To avoid math domain error, set income to min_income if below the minimum.
    if income < min_income:
        income = min_income
    income_index = (math.log(income) - math.log(min_income)) / (math.log(max_income) - math.log(min_income))
    # Bound the result to the [0, 1] range.
    return max(0, min(income_index, 1))


def calculate_hdi(life_expectancy: float, mean_years: float, expected_years: float, income: float):
    """
    Calculate the overall Human Development Index (HDI) along with
    individual sub-indices.
    """
    life_index = calculate_life_index(life_expectancy)
    education_index = calculate_education_index(mean_years, expected_years)
    income_index = calculate_income_index(income)

    # Geometric mean of the three indices
    hdi = (life_index * education_index * income_index) ** (1 / 3)
    return hdi, life_index, education_index, income_index


def classify_hdi(hdi: float) -> str:
    """
    Classify human development level based on the HDI value.
    Thresholds used (approximate):
      - Very High: HDI >= 0.800
      - High:      0.700 <= HDI < 0.800
      - Medium:    0.550 <= HDI < 0.700
      - Low:       HDI < 0.550
    """
    if hdi >= 0.800:
        return "Very High Human Development"
    elif hdi >= 0.700:
        return "High Human Development"
    elif hdi >= 0.550:
        return "Medium Human Development"
    else:
        return "Low Human Development"


def main():
    print("Human Development Index (HDI) Analyzer")
    print("----------------------------------------")

    try:
        # Read user inputs for the required indicators.
        life_expectancy = float(input("Enter life expectancy in years: "))
        mean_years = float(input("Enter mean years of schooling: "))
        expected_years = float(input("Enter expected years of schooling: "))
        income = float(input("Enter GNI per capita (in international dollars): "))
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values.")
        return

    # Calculate HDI and its sub-indices.
    hdi, life_index, education_index, income_index = calculate_hdi(life_expectancy, mean_years, expected_years, income)

    # Display the results.
    print("\nCalculated Indices:")
    print(f" Life Expectancy Index: {life_index:.4f}")
    print(f" Education Index:       {education_index:.4f}")
    print(f" Income Index:          {income_index:.4f}")
    print(f" Overall HDI:           {hdi:.4f}")
    classification = classify_hdi(hdi)
    print(f" Development Classification: {classification}")


if __name__ == '__main__':
    main()