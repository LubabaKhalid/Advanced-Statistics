import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Create individual sleep data points based on the counts
female_sleep = np.concatenate([np.full(3, 3), np.full(22, 4.5), np.full(26, 6.5), np.full(14, 8.5), np.full(4, 9.5)])
male_sleep = np.concatenate([np.full(8, 3), np.full(20, 4.5), np.full(37, 6.5), np.full(14, 8.5), np.full(2, 9.5)])

# Perform Wilcoxon Rank-Sum Test (Mann-Whitney U Test)
stat, p_value = stats.mannwhitneyu(female_sleep, male_sleep, alternative='two-sided')

# Boxplot visualization of sleep durations for males and females
plt.figure(figsize=(8, 6))
plt.boxplot([female_sleep, male_sleep], labels=['Females', 'Males'], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'), medianprops=dict(color='red'))

# Add title and labels
plt.title("Sleep Duration Distribution by Gender")
plt.ylabel("Sleep Duration (hrs)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

# Return the result of the test and conclusion
print("Wilcoxon Rank-Sum Test Statistic:", stat)
print("P-Value:", p_value)
