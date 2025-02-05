import numpy as np
import matplotlib.pyplot as plt

# Set parameters
num_samples = 100

# Generate independent standard normal random variables X and Y
X = np.random.normal(0, 1, num_samples)
Y = np.random.normal(0, 1, num_samples)

# Calculate Z = 1.5 + (2 * X / Y)
Z = 1.5 + (2 * X / Y)

# Plot the histogram
plt.hist(Z, bins=np.arange(-10, 15, 0.5), edgecolor='black', alpha=0.7)

# Set labels and title
plt.xlabel('Value of Z')
plt.ylabel('Frequency')
plt.title('Histogram of 100 Random Variables (Z = 1.5 + (2 * X / Y))')

# Show the plot
plt.show()

# Print the first few values of Z
print(Z[:10])
