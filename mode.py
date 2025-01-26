import matplotlib.pyplot as plt

# Data for screen time categories and their frequencies
categories = ["1 to 2 hours", "3 to 6 hours", "Less than 1 hour", "More than 6 hours", "None"]
frequencies = [38, 19.33, 21.33, 12.67, 8.67]  # Correcting percentages to numeric values

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, frequencies, color=['skyblue', 'salmon', 'lightgreen', 'orange', 'gray'])

# Add labels and title
plt.xlabel("Screen Time Categories", fontsize=12)
plt.title("Distribution of Screen Time Before Bedtime", fontsize=14)

# Annotate bars with their values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:.2f}%', ha='center', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
