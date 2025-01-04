from scipy.stats import kruskal

# Sleep quality scores for each work schedule
day_classes_only = [4, 25, 25, 24, 9]
Com_day_evening_classes = [2,4,11,4,3]
evening_classes_only = [0,0,2,0,1]
job=[1,3,7,6,1]
online_classes=[0,0,2,0,0]


# Perform Kruskal-Wallis test
stat, p = kruskal(Com_day_evening_classes,day_classes_only,evening_classes_only,job,online_classes)

# Output results
print("Kruskal-Wallis H-statistic:", stat)
print("P-value:", p)

# Interpretation
alpha = 0.05
if p < alpha:
    print("Significant differences found. Reject the null hypothesis.")
else:
    print("No significant differences. Fail to reject the null hypothesis.")