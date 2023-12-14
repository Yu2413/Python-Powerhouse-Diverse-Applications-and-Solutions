import matplotlib.pyplot as plt
import numpy as np

# Example data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.random.randint(100, 500, len(months))

plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='blue')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
