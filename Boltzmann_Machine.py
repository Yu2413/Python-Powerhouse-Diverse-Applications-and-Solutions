import numpy as np

class BoltzmannMachine:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.weights = np.random.rand(num_nodes, num_nodes) - 0.5
        self.weights = 0.5 * (self.weights + self.weights.T)  # Make the matrix symmetric
        np.fill_diagonal(self.weights, 0)  # No self-connections

    def energy(self, state):
        return -0.5 * np.dot(state, np.dot(self.weights, state))

    def sample(self):
        state = np.random.choice([0, 1], size=self.num_nodes)
        for _ in range(100):  # Sampling iterations
            i = np.random.randint(0, self.num_nodes)
            activation = np.dot(self.weights[i], state)
            probability = 1 / (1 + np.exp(-activation))
            state[i] = 1 if np.random.rand() < probability else 0
        return state

    def train(self, data, epochs, learning_rate):
        for epoch in range(epochs):
            for sample in data:
                # Data phase
                positive_correlations = np.outer(sample, sample)
                # Model phase
                state = self.sample()
                negative_correlations = np.outer(state, state)

                # Update weights
                self.weights += learning_rate * (positive_correlations - negative_correlations)
                np.fill_diagonal(self.weights, 0)  # No self-connections

# Example usage
num_nodes = 10
bm = BoltzmannMachine(num_nodes)

# Dummy data
data = np.random.choice([0, 1], (5, num_nodes))

# Training
bm.train(data, epochs=100, learning_rate=0.1)
