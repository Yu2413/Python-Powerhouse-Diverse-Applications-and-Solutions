import numpy as np
import matplotlib.pyplot as plt


# Define the payoff function for a standard call option
def call_payoff(S, K):
    """
    Payoff of a standard call option.

    Parameters:
        S (array_like): Underlying asset prices.
        K (float): Strike price of the call option.

    Returns:
        array_like: Payoff values.
    """
    return np.maximum(S - K, 0)


# Define the payoff function for a compound call option (call on a call)
def compound_call_payoff(S, K_call, K_compound):
    """
    Payoff of a compound call option, which gives the right to buy a call option.

    Parameters:
        S (array_like): Underlying asset prices at decision time.
        K_call (float): Strike price of the underlying call option.
        K_compound (float): Strike price of the compound call option.

    Returns:
        array_like: Payoff of the compound call option.
    """
    # First, compute the payoff of the underlying call option
    underlying_call = call_payoff(S, K_call)
    # The compound call option gives the right to acquire the call for a premium K_compound.
    # Its payoff is the underlying call payoff minus K_compound, floored at 0.
    return np.maximum(underlying_call - K_compound, 0)


# Parameters
K_call = 100  # Strike of the underlying call option
K_compound = 10  # Strike (premium) for the compound option
S_min, S_max = 0, 200
S = np.linspace(S_min, S_max, 400)

# Compute payoffs
payoff_call = call_payoff(S, K_call)
payoff_compound = compound_call_payoff(S, K_call, K_compound)

# Plotting the payoffs
plt.figure(figsize=(10, 6))
plt.plot(S, payoff_call, label=f'Call Option Payoff (K={K_call})', linewidth=2)
plt.plot(S, payoff_compound, label=f'Compound Call Option Payoff (K_compound={K_compound})', linewidth=2)
plt.xlabel('Underlying Asset Price at Decision Time')
plt.ylabel('Payoff')
plt.title('Payoff Diagram for a Compound Call Option (Call on a Call)')
plt.legend()
plt.grid(True)
plt.show()
