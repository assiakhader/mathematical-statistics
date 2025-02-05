import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set parameters
mean = 1.5
std_dev = 2
num_samples = 100
sample_size = 20

# Simulate 100 sample means by averaging 20 random normal variables each time
sample_means = np.array([np.mean(np.random.normal(mean, std_dev, sample_size)) for _ in range(num_samples)])

# Count how many sample means are bigger than 0
num_above_zero = np.sum(sample_means > 0)

# Estimate the probability
estimate_prob = num_above_zero / num_samples

# Theoretical probability using Central Limit Theorem
sample_std_dev = std_dev / np.sqrt(sample_size)  # Standard deviation of the sample mean
theoretical_prob = 1 - norm.cdf(0, mean, sample_std_dev)

# Set the range and interval for the histogram
bin_edges = np.arange(-4, 10.5, 0.5)

# Plot the histogram
plt.hist(sample_means, bins=bin_edges, edgecolor='black', alpha=0.7)

# Mark the area for the estimate (sample means > 0)
plt.fill_between(bin_edges[:-1], 0, np.histogram(sample_means, bins=bin_edges)[0], where=(bin_edges[:-1] > 0), color='blue', alpha=0.5, label="Estimate Area")

# Set labels and title
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.title(f'Histogram of 100 Sample Means\nEstimate: {estimate_prob:.2f}, Theoretical: {theoretical_prob:.2f}')

# Show the plot
plt.legend()
plt.show()

# Output the results
print(f'Number of sample means greater than 0: {num_above_zero}')
print(f'Estimated probability: {estimate_prob:.2f}')
print(f'Theoretical probability: {theoretical_prob:.2f}')
