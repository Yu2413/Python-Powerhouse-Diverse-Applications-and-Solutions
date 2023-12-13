# plot_examples.py
import matplotlib.pyplot as plt

def plot_line_graph(x, y):
    plt.plot(x, y)
    plt.title('Simple Line Graph')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.show()

# Example data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plot_line_graph(x, y)
