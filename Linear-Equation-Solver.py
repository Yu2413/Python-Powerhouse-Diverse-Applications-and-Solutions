# linear_algebra.py
import numpy as np
from scipy.linalg import solve

def solve_linear_equation(A, b):
    """
    Solves the linear equation A * x = b
    :param A: 2D array representing the coefficients matrix
    :param b: 1D array representing the constants
    :return: Solution array
    """
    x = solve(A, b)
    return x

# Example usage
if __name__ == "__main__":
    # Coefficients matrix
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])

    # Constants
    b = np.array([1, -2, 0])

    # Solve the system of equations
    solution = solve_linear_equation(A, b)
    print("Solution of the system:", solution)
