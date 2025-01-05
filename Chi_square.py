import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
categories = ['No Diagnosis', 'Diagnosed']
medication = [8, 7]
no_medication = [107, 28]

x = np.arange(len(categories))  # label locations
width = 0.35  # width of the bars

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width / 2, medication, width, label='Medication', color='skyblue')
bars2 = ax.bar(x + width / 2, no_medication, width, label='No Medication', color='salmon')

# Add labels, title, and legend
ax.set_xlabel('Sleep Disorder Diagnosis', fontsize=12)
ax.set_ylabel('Number of Participants', fontsize=12)
ax.set_title('Medication Use vs Sleep Disorder Diagnosis', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend()

# Annotate bars with their values
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', fontsize=10)

# Display the chart
plt.tight_layout()
plt.show()
