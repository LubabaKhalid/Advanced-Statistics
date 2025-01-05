import numpy as np
import scipy.stats as stats

# Example binary sequence: 1 represents frequent urination at night, 0 represents infrequent
urination_responses = [1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1]
print(len(urination_responses))

# Function to perform Runs Test for Randomness
def runs_test(data):
    n = len(data)
    # Count the number of runs
    runs = 1  # Start with one run
    for i in range(1, n):
        if data[i] != data[i - 1]:
            runs += 1

    # Calculate expected number of runs
    p1 = np.sum(data) / n  # Proportion of 1s
    p0 = 1 - p1  # Proportion of 0s

    # Avoiding division by zero or very small numbers causing invalid variance
    if p1 == 0 or p0 == 0:
        return runs, 0, np.nan  # If all 0's or all 1's, we cannot calculate variance

    expected_runs = 1 + (2 * p1 * p0 * n) / (n - 1)

    # Calculate the variance of the runs
    var_runs = (2 * p1 * p0 * (2 * p1 * p0 * n - n)) / (n - 1)

    # Handle case where variance is very small or negative
    if var_runs <= 0:
        return runs, expected_runs, np.nan

    z = (runs - expected_runs) / np.sqrt(var_runs)

    # Perform the test
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # Two-tailed test

    return runs, expected_runs, p_value

# Perform the Runs Test
runs, expected_runs, p_value = runs_test(urination_responses)

# Output results
print(f"Observed Runs: {runs}")
print(f"Expected Runs: {expected_runs:.2f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Significant departure from randomness. Reject the null hypothesis.")
else:
    print("No significant departure from randomness. Fail to reject the null hypothesis.")
