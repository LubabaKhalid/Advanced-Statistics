# Re-import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data for screen time categories
categories = ["1 to 2 hours", "3 to 6 hours", "Less than 1 hour", "More than 6 hours", "No screen time"]
females = [30, 15, 18, 7, 3]
males = [27, 14, 14, 12, 10]

# Create positions for the bars
x = np.arange(len(categories))
width = 0.35

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, females, width, label='Females', color='lightblue')
plt.bar(x + width/2, males, width, label='Males', color='orange')

# Add labels and title
plt.xlabel("Screen Time Categories")
plt.ylabel("Number of Participants")
plt.title("Screen Time Before Bedtime by Gender")
plt.xticks(x, categories)
plt.legend()

# Display the chart
plt.tight_layout()
plt.show()
