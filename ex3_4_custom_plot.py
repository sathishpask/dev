import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data with custom styles
ax.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
ax.plot(x, y2, label='Cosine Wave', color='red', linestyle='-', linewidth=2)

# Customize axes labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Customized Sine and Cosine Waves')

# Add a legend
ax.legend()

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
