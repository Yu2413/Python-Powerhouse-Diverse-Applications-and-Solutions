import math
from math import log, sqrt, exp
from scipy.stats import norm


def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes-Merton option price.

    Parameters:
    S : float
        Current price of the underlying asset.
    K : float
        Strike price of the option.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate (annualized).
    sigma : float
        Volatility of the underlying asset (annualized).
    option_type : str, optional
        'call' for call option, 'put' for put option. Default is 'call'.

    Returns:
    float
        The option price.
    """
    # Calculate d1 and d2 using the Black-Scholes formulas
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    if option_type.lower() == 'call':
        option_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == 'put':
        option_price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be either 'call' or 'put'")

    return option_price


# Example usage:
S = 100  # Current asset price
K = 100  # Strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate (5% for .05)
sigma = 0.2  # Volatility (20% for .2)

call_price = black_scholes(S, K, T, r, sigma, option_type='call')
put_price = black_scholes(S, K, T, r, sigma, option_type='put')

print("Call Option Price:", call_price)
print("Put Option Price:", put_price)