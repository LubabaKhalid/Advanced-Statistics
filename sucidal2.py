# Re-importing necessary libraries due to reset
import matplotlib.pyplot as plt
import numpy as np

# Data preparation for stacked bar chart
categories = ['Not at all', 'Several days', 'More than half the days', 'Nearly every day']
percentage_labels = ['20%', '40%', '60%', '80%', '100%', 'None']

# Data for the categories
not_at_all = [10, 10, 11, 2, 6, 13]
several_days = [20, 19, 13, 2, 2, 14]
more_than_half_the_days = [5, 6, 2, 2, 3, 1]
nearly_every_day = [0, 3, 2, 2, 1, 1]

data = np.array([
    not_at_all,
    several_days,
    more_than_half_the_days,
    nearly_every_day
])

# Creating stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_positions = np.arange(len(percentage_labels))

# Plot each category as a stack
colors = ['skyblue', 'mediumspringgreen', 'sandybrown', 'violet']
for i, category in enumerate(categories):
    ax.bar(bar_positions, data[i], label=category, color=colors[i], bottom=data[:i].sum(axis=0))

# Adding titles and labels
ax.set_title("Stacked Bar Chart: Anxiety/Depression Levels vs Belief in Sleep Disorders", fontsize=14)
ax.set_xlabel("Percentage Belief in Sleep Disorders Leading to Suicidal Risk", fontsize=12)
ax.set_ylabel("Frequency of Responses", fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(percentage_labels)
ax.legend(title="Anxiety/Depression Levels")

plt.tight_layout()
plt.show()
