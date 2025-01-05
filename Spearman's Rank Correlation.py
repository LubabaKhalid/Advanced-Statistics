import matplotlib.pyplot as plt

# Data
percentages = [20, 40, 60, 80, 100, 'None']
not_at_all = [10, 10, 11, 2, 6, 13]
several_days = [20, 19, 13, 2, 2, 14]
more_than_half_the_days = [5, 6, 2, 2, 3, 1]
nearly_every_day = [0, 3, 2, 2, 1, 1]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(percentages, not_at_all, marker='o', label='Not at all', color='blue')
ax.plot(percentages, several_days, marker='o', label='Several days', color='green')
ax.plot(percentages, more_than_half_the_days, marker='o', label='More than half the days', color='orange')
ax.plot(percentages, nearly_every_day, marker='o', label='Nearly every day', color='red')

# Adding titles and labels
ax.set_title("Anxiety and Depression Levels vs Belief in Sleep Disorders Causing Suicidal Risks", fontsize=14)
ax.set_xlabel("Percentage Belief in Sleep Disorders Leading to Suicidal Risk", fontsize=12)
ax.set_ylabel("Frequency of Anxiety/Depression Levels", fontsize=12)
ax.legend()

plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
