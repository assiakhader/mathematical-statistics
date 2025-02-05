import numpy as np
import matplotlib.pyplot as plt

# Set parameters
num_samples = 100

# Generate independent standard normal random variables X and Y
X = np.random.normal(0, 1, num_samples)
Y = np.random.normal(0, 1, num_samples)

# Calculate Z = 1.5 + (2 * X / Y)
Z = 1.5 + (2 * X / Y)

# Plot the histogramimport numpy as np
import matplotlib.pyplot as plt

# Set parameters
num_samples = 100

# Generate independent standard normal random variables X and Y
X = np.random.normal(0, 1, num_samples)
Y = np.random.normal(0, 1, num_samples)

# Calculate Z = 1.5 + (2 * X / Y)
Z = 1.5 + (2 * X / Y)

# Estimate the probability that Z > 0
probability_estimate = np.sum(Z > 0) / num_samples

# Theoretical probability for a Cauchy distribution with location 1.5 and scale 2
theoretical_probability = 0.5  # As explained earlier

# Plot the histogram
plt.hist(Z, bins=np.arange(-10, 15, 0.5), edgecolor='black', alpha=0.7)

# Add the shaded area indicating the estimate
plt.hist(Z[Z > 0], bins=np.arange(0, 15, 0.5), edgecolor='blue', alpha=0.3, label='Estimate Area')

# Set labels and title
plt.xlabel('Value of Z')
plt.ylabel('Frequency')
plt.title(f'Histogram of 100 Random Variables (Z = 1.5 + (2 * X / Y))')

# Show the plot with the legend
plt.legend()
plt.show()

# Print the estimate and theoretical probability
print(f"Estimated probability (Z > 0): {probability_estimate:.2f}")
print(f"Theoretical probability (Z > 0): {theoretical_probability:.2f}")

plt.hist(Z, bins=np.arange(-10, 15, 0.5), edgecolor='black', alpha=0.7)

# Set labels and title
plt.xlabel('Value of Z')
plt.ylabel('Frequency')
plt.title('Histogram of 100 Random Variables (Z = 1.5 + (2 * X / Y))')

# Show the plot
plt.show()

# Print the first few values of Z
print(Z[:10])
