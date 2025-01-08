# Re-import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
sleep_quality = ['Very Poor', 'Poor', 'Fair', 'Good', 'Very Good']
gpa_impact = [10, 39, 49, 37, 15]

# Create a DataFrame
data = pd.DataFrame({
    'Sleep Quality': sleep_quality,
    'GPA Impact': gpa_impact
})

# Assign ranks to the sleep quality and GPA impact
data['Sleep Quality Rank'] = data['Sleep Quality'].map({'Very Poor': 1, 'Poor': 2, 'Fair': 3, 'Good': 4, 'Very Good': 5})
data['GPA Impact Rank'] = pd.Series(gpa_impact).rank()

# Visualization of Sleep Quality vs. GPA Impact ranks
sleep_quality_rank = data['Sleep Quality Rank']
gpa_impact_rank = data['GPA Impact Rank']

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(sleep_quality_rank, gpa_impact_rank, color='blue', label="Data Points")
plt.plot(sleep_quality_rank, gpa_impact_rank, linestyle='--', color='gray', alpha=0.7, label="Trend Line")

# Add labels, title, and grid
plt.title("Relationship Between Sleep Quality and GPA Impact (Ranks)", fontsize=14)
plt.xlabel("Sleep Quality Rank", fontsize=12)
plt.ylabel("GPA Impact Rank", fontsize=12)
plt.xticks(sleep_quality_rank, sleep_quality, rotation=45)
plt.grid(alpha=0.5)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
