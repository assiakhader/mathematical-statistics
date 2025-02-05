import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set parameters
mean = 1.5
std_dev = 2
num_samples = 100

# Simulate 100 random normal variables
data = np.random.normal(mean, std_dev, num_samples)

# Count how many variables are bigger than 0
num_above_zero = np.sum(data > 0)

# Estimate the probability
estimate_prob = num_above_zero / num_samples

# Theoretical probability using CDF for normal distribution
theoretical_prob = 1 - norm.cdf(0, mean, std_dev)

# Set the range and interval for the histogram
bin_edges = np.arange(-4, 10.5, 0.5)

# Plot the histogram
plt.hist(data, bins=bin_edges, edgecolor='black', alpha=0.7)

# Mark the area for the estimate
plt.fill_between(bin_edges[:-1], 0, np.histogram(data, bins=bin_edges)[0], where=(bin_edges[:-1] > 0), color='blue', alpha=0.5, label="Estimate Area")

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Histogram of 100 Random Normal Variables\nEstimate: {estimate_prob:.2f}, Theoretical: {theoretical_prob:.2f}')

# Show the plot
plt.legend()
plt.show()

# Output the results
print(f'Number of values greater than 0: {num_above_zero}')
print(f'Estimated probability: {estimate_prob:.2f}')
print(f'Theoretical probability: {theoretical_prob:.2f}')
