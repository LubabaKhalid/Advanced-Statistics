import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Screen time data for each age group
age_groups = ["10-18", "19-24", "25-35", "35-50"]
screen_time_10_18 = [3, 3, 6, 2, 2]  # None, <1 hour, 1-2 hours, 3-6 hours, >6 hours
screen_time_19_24 = [8, 20, 37, 25, 14]
screen_time_25_35 = [1, 8, 11, 2, 3]
screen_time_35_50 = [1, 0, 1, 0, 0]

# Convert data into a flattened format for ANOVA
group_10_18 = np.repeat(age_groups[0], np.sum(screen_time_10_18))
group_19_24 = np.repeat(age_groups[1], np.sum(screen_time_19_24))
group_25_35 = np.repeat(age_groups[2], np.sum(screen_time_25_35))
group_35_50 = np.repeat(age_groups[3], np.sum(screen_time_35_50))

# Reconstruct data based on frequencies for ANOVA
data_10_18 = np.concatenate([np.repeat("None", screen_time_10_18[0]),
                             np.repeat("<1 hour", screen_time_10_18[1]),
                             np.repeat("1-2 hours", screen_time_10_18[2]),
                             np.repeat("3-6 hours", screen_time_10_18[3]),
                             np.repeat(">6 hours", screen_time_10_18[4])])

data_19_24 = np.concatenate([np.repeat("None", screen_time_19_24[0]),
                             np.repeat("<1 hour", screen_time_19_24[1]),
                             np.repeat("1-2 hours", screen_time_19_24[2]),
                             np.repeat("3-6 hours", screen_time_19_24[3]),
                             np.repeat(">6 hours", screen_time_19_24[4])])

data_25_35 = np.concatenate([np.repeat("None", screen_time_25_35[0]),
                             np.repeat("<1 hour", screen_time_25_35[1]),
                             np.repeat("1-2 hours", screen_time_25_35[2]),
                             np.repeat("3-6 hours", screen_time_25_35[3]),
                             np.repeat(">6 hours", screen_time_25_35[4])])

data_35_50 = np.concatenate([np.repeat("None", screen_time_35_50[0]),
                             np.repeat("<1 hour", screen_time_35_50[1]),
                             np.repeat("1-2 hours", screen_time_35_50[2]),
                             np.repeat("3-6 hours", screen_time_35_50[3]),
                             np.repeat(">6 hours", screen_time_35_50[4])])

# Perform ANOVA test
stat, p_value = stats.f_oneway(screen_time_10_18, screen_time_19_24, screen_time_25_35, screen_time_35_50)

# Plotting the data for visualization
x = np.arange(len(age_groups))
mean_values = [np.mean(screen_time_10_18),
               np.mean(screen_time_19_24),
               np.mean(screen_time_25_35),
               np.mean(screen_time_35_50)]

plt.bar(x, mean_values, color=['blue', 'green', 'orange', 'red'], alpha=0.7)
plt.xticks(x, age_groups)
plt.ylabel("Average Screen Time (arbitrary units)")
plt.title("Average Screen Time Across Age Groups")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the graph
plt.show()

# Results summary
print(stat, p_value)
