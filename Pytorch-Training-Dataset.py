# neural_network.py
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # 10 input features, 5 output features
        self.fc2 = nn.Linear(5, 2)   # 5 input features, 2 output features

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the network, optimizer, and loss function
net = SimpleNet()
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.MSELoss()

# Dummy dataset
inputs = torch.randn(100, 10)  # 100 samples, 10 features each
targets = torch.randn(100, 2)  # 100 samples, 2 target values each

# Training loop
for epoch in range(100):  # 100 epochs
    optimizer.zero_grad()   # Zero the gradient buffers
    outputs = net(inputs)  # Forward pass
    loss = criterion(outputs, targets)  # Compute the loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

print('Training complete')
