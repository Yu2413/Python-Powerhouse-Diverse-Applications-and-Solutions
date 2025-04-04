"""
FOREX-BASED RECESSION LIKELIHOOD ANALYSIS

This script demonstrates a simple workflow for:
1. Loading (synthetic) FOREX and economic data
2. Generating features
3. Training a basic machine learning model to classify the likelihood of a recession
4. Visualizing some results

Disclaimers:
- This script uses synthetic/random data purely for demonstration.
- Real-world data and domain expertise are critical to making meaningful predictions.
- This code does not guarantee the correctness of any financial decisions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


# -------------------------------------------------------------
# 1. DATA GENERATION / LOADING
# -------------------------------------------------------------
def generate_synthetic_forex_data(num_samples=200):
    """
    Generates synthetic FOREX data for demonstration.
    Returns a DataFrame with columns:
        - Date:              chronological timestamps
        - EUR_USD:           synthetic EUR/USD exchange rate
        - GBP_USD:           synthetic GBP/USD exchange rate
        - USD_JPY:           synthetic USD/JPY exchange rate
        - Economic_Indicator synthetic economic variable (e.g. growth index)
        - Recession_Flag:    1 if economy is in recession, 0 otherwise
    """
    np.random.seed(42)  # for reproducibility

    date_range = pd.date_range(start='2015-01-01', periods=num_samples, freq='M')

    # Generate some random walk-like data for forex rates
    eur_usd = np.cumsum(np.random.normal(0, 0.1, size=num_samples)) + 1.10
    gbp_usd = np.cumsum(np.random.normal(0, 0.1, size=num_samples)) + 1.50
    usd_jpy = np.cumsum(np.random.normal(0, 0.5, size=num_samples)) + 110.0

    # Generate synthetic economic indicator (like a composite index)
    economic_indicator = np.cumsum(np.random.normal(0, 0.02, size=num_samples)) + 0.0

    # Recession flag triggered by some random condition
    recession_flag = (economic_indicator < -0.5).astype(int)

    df = pd.DataFrame({
        'Date': date_range,
        'EUR_USD': eur_usd,
        'GBP_USD': gbp_usd,
        'USD_JPY': usd_jpy,
        'Economic_Indicator': economic_indicator,
        'Recession_Flag': recession_flag
    })

    return df


def main():
    # Generate synthetic data
    df = generate_synthetic_forex_data(300)

    # Sort by date (just to be sure)
    df.sort_values(by='Date', inplace=True)

    # -------------------------------------------------------------
    # 2. FEATURE ENGINEERING
    # -------------------------------------------------------------
    # Example: We calculate daily (month-to-month) returns or changes
    # from one row to the next as a proxy for volatility or trend.
    df['EUR_USD_change'] = df['EUR_USD'].pct_change().fillna(0)
    df['GBP_USD_change'] = df['GBP_USD'].pct_change().fillna(0)
    df['USD_JPY_change'] = df['USD_JPY'].pct_change().fillna(0)
    df['Economic_Change'] = df['Economic_Indicator'].diff().fillna(0)

    # For classification, we'll define the Recession_Flag as our target
    features = ['EUR_USD_change', 'GBP_USD_change', 'USD_JPY_change', 'Economic_Change']
    target = 'Recession_Flag'

    # Drop any rows with NaNs after feature engineering (if any remain)
    df.dropna(subset=features + [target], inplace=True)

    # -------------------------------------------------------------
    # 3. SPLIT DATA AND TRAIN A BASIC MODEL
    # -------------------------------------------------------------
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42,
                                                        stratify=y)

    # Simple RandomForest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # -------------------------------------------------------------
    # 4. EVALUATE AND INTERPRET RESULTS
    # -------------------------------------------------------------
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Feature Importance
    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({
        'Feature': features,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    print("Feature Importances:")
    print(feature_importance_df)

    # -------------------------------------------------------------
    # 5. BASIC VISUALIZATIONS
    # -------------------------------------------------------------
    # Plot the synthetic economic indicator over time
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Economic_Indicator'])
    plt.title('Synthetic Economic Indicator Over Time')
    plt.xlabel('Date')
    plt.ylabel('Indicator Value')
    plt.show()

    # Plot the FOREX rates over time
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['EUR_USD'], label='EUR/USD')
    plt.plot(df['Date'], df['GBP_USD'], label='GBP/USD')
    plt.plot(df['Date'], df['USD_JPY'], label='USD/JPY')
    plt.title('Synthetic FOREX Rates Over Time')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.legend()
    plt.show()

    # Plot actual vs predicted recession flags
    plt.figure(figsize=(10, 5))
    plt.plot(df.loc[X_test.index, 'Date'], y_test, label='Actual Recession')
    plt.plot(df.loc[X_test.index, 'Date'], y_pred, label='Predicted Recession')
    plt.title('Actual vs. Predicted Recession Periods')
    plt.xlabel('Date')
    plt.ylabel('Recession Flag')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
