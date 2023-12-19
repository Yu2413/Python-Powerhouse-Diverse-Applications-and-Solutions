import numpy as np

class RestrictedBoltzmannMachine:

    def __init__(self, num_visible, num_hidden):
        self.num_visible = num_visible
        self.num_hidden = num_hidden

        # Initialize weights and biases
        self.weights = np.random.randn(num_visible, num_hidden) * 0.1
        self.visible_bias = np.zeros(num_visible)  # Bias for visible layer
        self.hidden_bias = np.zeros(num_hidden)    # Bias for hidden layer

    def sample_hidden(self, visible):
        # Calculate activations of the hidden layer
        hidden_activations = np.dot(visible, self.weights) + self.hidden_bias
        # Calculate probabilities of turning the hidden units on.
        hidden_probs = self._sigmoid(hidden_activations)
        # Turn the hidden units on with their specific probabilities
        hidden_states = (hidden_probs > np.random.rand(self.num_hidden)).astype(int)
        return hidden_states

    def sample_visible(self, hidden):
        # Calculate activations of the visible layer
        visible_activations = np.dot(hidden, self.weights.T) + self.visible_bias
        # Calculate probabilities of turning the visible units on.
        visible_probs = self._sigmoid(visible_activations)
        # Turn the visible units on with their specific probabilities
        visible_states = (visible_probs > np.random.rand(self.num_visible)).astype(int)
        return visible_states

    def train(self, data, epochs, learning_rate):
        num_samples = data.shape[0]

        for epoch in range(epochs):
            # Randomize the order of inputs
            np.random.shuffle(data)

            for sample in data:
                v0 = np.array(sample)  # Start with a training sample

                # Contrastive Divergence
                h0 = self.sample_hidden(v0)
                v1 = self.sample_visible(h0)
                h1 = self.sample_hidden(v1)

                # Update weights and biases
                self.weights += learning_rate * (np.outer(v0, h0) - np.outer(v1, h1)) / num_samples
                self.visible_bias += learning_rate * (v0 - v1) / num_samples
                self.hidden_bias += learning_rate * (h0 - h1) / num_samples

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

# Example usage
num_visible = 6  # Number of visible nodes
num_hidden = 3   # Number of hidden nodes

rbm = RestrictedBoltzmannMachine(num_visible, num_hidden)

# Example data: 6 binary features
data = np.random.randint(2, size=(10, num_visible))

# Train the RBM
rbm.train(data, epochs=5000, learning_rate=0.05)
