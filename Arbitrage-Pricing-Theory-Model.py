class APTModel:
    def __init__(self, risk_free_rate, factors):
        """
        Initialize the APT Model.

        Parameters:
            risk_free_rate (float): The risk free rate.
            factors (dict): A dictionary mapping factor names to their risk premiums.
        """
        self.risk_free_rate = risk_free_rate
        self.factors = factors

    def expected_return(self, betas):
        """
        Calculate the expected return for an asset given its factor betas.

        Parameters:
            betas (dict): A dictionary mapping factor names to the asset's beta.

        Returns:
            float: The expected return calculated using the APT model.
        """
        ret = self.risk_free_rate
        for factor, beta in betas.items():
            if factor in self.factors:
                ret += beta * self.factors[factor]
            else:
                print(f"Warning: Factor '{factor}' not found in the model factors.")
        return ret


def main():
    # Input the risk free rate.
    risk_free_rate = float(input("Enter the risk free rate (e.g., 0.02 for 2%): "))

    # Input the factors and their corresponding risk premiums.
    factors = {}
    num_factors = int(input("Enter the number of factors: "))
    for i in range(num_factors):
        factor_name = input(f"Enter name for factor {i + 1}: ")
        risk_premium = float(input(f"Enter the risk premium for '{factor_name}' (e.g., 0.03 for 3%): "))
        factors[factor_name] = risk_premium

    # Create an instance of the APT model.
    apt_model = APTModel(risk_free_rate, factors)

    # Optionally, input multiple assets.
    num_assets = int(input("Enter the number of assets to evaluate: "))
    for j in range(num_assets):
        print(f"\nEntering data for asset {j + 1}:")
        betas = {}
        # For each factor, input the corresponding beta.
        for factor in factors.keys():
            beta_value = float(input(f"Enter beta for factor '{factor}': "))
            betas[factor] = beta_value

        # Calculate and display the expected return.
        exp_return = apt_model.expected_return(betas)
        print(f"Expected return for asset {j + 1}: {exp_return:.4f}")


if __name__ == '__main__':
    main()
