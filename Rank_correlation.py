import pandas as pd
from scipy.stats import spearmanr

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

# Display the DataFrame
print(data)

# Calculate Spearman's rank correlation
correlation, p_value = spearmanr(data['Sleep Quality Rank'], data['GPA Impact Rank'])

# Display the results
print(f'Spearman correlation coefficient: {correlation:.4f}')
print(f'P-value: {p_value:.4f}')