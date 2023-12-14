import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

# Sample data
X = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float32)
y = torch.tensor([0, 1, 1, 0], dtype=torch.float32)

# Create dataset and dataloader
dataset = TensorDataset(X, y.view(-1, 1))
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Define the Neural Network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 3)  # Input layer to hidden layer
        self.fc2 = nn.Linear(3, 1)  # Hidden layer to output layer

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

model = SimpleNN()

# Define Loss Function and Optimizer
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000):
    for inputs, targets in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Test the model
with torch.no_grad():
    test_data = torch.tensor([[0.5, 0.5]], dtype=torch.float32)
    prediction = model(test_data)
    print(f"Prediction for [0.5, 0.5]: {prediction.item()}")
