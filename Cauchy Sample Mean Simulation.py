import numpy as np
import matplotlib.pyplot as plt

# Set parameters
num_samples = 100
sample_size = 20

# Generate independent standard normal random variables X and Y
X = np.random.normal(0, 1, (num_samples, sample_size))
Y = np.random.normal(0, 1, (num_samples, sample_size))

# Calculate the sample means Z = 1.5 + (2 * X / Y)
Z_sample_means = 1.5 + (2 * X / Y)
sample_means = Z_sample_means.mean(axis=1)  # Taking the average across each sample

# Estimate the probability that the sample mean is greater than 0
probability_estimate = np.sum(sample_means > 0) / num_samples

# Theoretical probability for a Cauchy distribution with location 1.5 and scale 2
theoretical_probability = 0.5  # As explained earlier

# Plot the histogram
plt.hist(sample_means, bins=np.arange(-10, 15, 0.5), edgecolor='black', alpha=0.7)

# Add the shaded area indicating the estimate
plt.hist(sample_means[sample_means > 0], bins=np.arange(0, 15, 0.5), edgecolor='blue', alpha=0.3, label='Estimate Area')

# Set labels and title
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.title(f'Histogram of 100 Sample Means (Z = 1.5 + (2 * X / Y))')

# Show the plot with the legend
plt.legend()
plt.show()

# Print the estimate and theoretical probability
print(f"Estimated probability (Sample Mean > 0): {probability_estimate:.2f}")
print(f"Theoretical probability (Sample Mean > 0): {theoretical_probability:.2f}")
