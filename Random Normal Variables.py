import numpy as np
import matplotlib.pyplot as plt

# Set parameters
mean = 1.5
std_dev = 2
num_samples = 100

# Simulate 100 random normal variables
data = np.random.normal(mean, std_dev, num_samples)

# Set the range and interval for the histogram
bin_edges = np.arange(-4, 10.5, 0.5)  # Class intervals of length 0.5 from -4 to 10

# Plot the histogram
plt.hist(data, bins=bin_edges, edgecolor='black', alpha=0.7)

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 100 Random Normal Variables')

# Show the plot
plt.show()
