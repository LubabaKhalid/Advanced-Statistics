import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for enhanced visualizations

# Data
day_classes_only = [4, 25, 25, 24, 9]
Com_day_evening_classes = [2, 4, 11, 4, 3]
evening_classes_only = [0, 0, 2, 0, 1]
job = [1, 3, 7, 6, 1]
online_classes = [0, 0, 2, 0, 0]

# Combine data into a list for plotting
data = [day_classes_only, Com_day_evening_classes, evening_classes_only, job, online_classes]

# Labels for each group
labels = ['Day Classes', 'Day + Evening Classes', 'Evening Classes', 'Job', 'Online Classes']

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, inner="quartile", palette="muted")

# Add title and axis labels
plt.title("Distribution of Sleep Quality Scores Across Work Schedules", fontsize=14)
plt.xlabel("Work Schedules", fontsize=12)
plt.ylabel("Sleep Quality Scores", fontsize=12)

# Show the grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.xticks(ticks=range(len(labels)), labels=labels)  # Set x-tick labels
plt.show()