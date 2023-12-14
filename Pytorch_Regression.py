import torch
import torch.nn as nn
import numpy as np

# Synthetic data
x_train = np.linspace(-1, 1, 101)
y_train = 2 * x_train + np.random.randn(*x_train.shape) * 0.33

# Convert to PyTorch tensors
x_train = torch.from_numpy(x_train).float()
y_train = torch.from_numpy(y_train).float()

# Reshape for batch compatibility
x_train = x_train.view(-1, 1)
y_train = y_train.view(-1, 1)

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # One input and one output

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x to the model
    pred_y = model(x_train)

    # Compute and print loss
    loss = criterion(pred_y, y_train)

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Predict
x_test = torch.linspace(-1, 1, 101).view(-1, 1).float()
predicted_values = model(x_test)

# Convert predictions to NumPy for display
predicted_values = predicted_values.detach().numpy()

# Print predictions
print(predicted_values)
