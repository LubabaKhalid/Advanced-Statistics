import matplotlib.pyplot as plt
import numpy as np

# Data
day_classes_only = [4, 25, 25, 24, 9]
Com_day_evening_classes = [2, 4, 11, 4, 3]
evening_classes_only = [0, 0, 2, 0, 1]
job = [1, 3, 7, 6, 1]
online_classes = [0, 0, 2, 0, 0]

# Combine data into a list for calculations
data = [day_classes_only, Com_day_evening_classes, evening_classes_only, job, online_classes]

# Labels for each group
labels = ['Day Classes', 'Day + Evening Classes', 'Evening Classes', 'Job', 'Online Classes']

# Calculate means and standard deviations
means = [np.mean(group) for group in data]
std_devs = [np.std(group, ddof=1) for group in data]  # ddof=1 for sample standard deviation

# Create the bar chart
plt.figure(figsize=(10, 6))
x_positions = np.arange(len(labels))
plt.bar(x_positions, means, yerr=std_devs, color='skyblue', capsize=5, alpha=0.8)

# Add titles and labels
plt.title("Average Sleep Quality Scores with Variability by Work Schedule", fontsize=14)
plt.xlabel("Work Schedules", fontsize=12)
plt.ylabel("Average Sleep Quality Score", fontsize=12)

# Add x-axis tick labels
plt.xticks(x_positions, labels, fontsize=10)

# Show the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
