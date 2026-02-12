python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Indices_Summary_Jan2026.csv')

# Basic data overview
print(data.head())

# Filter data for FADX 15 index
fadx15_data = data[data['Index'] == 'FADX 15']

# Plot daily closing values
plt.figure(figsize=(10, 5))
plt.plot(fadx15_data['Date'], fadx15_data['Close'], marker='o', label='FADX 15 Closing Values')
plt.title('Daily Closing Values of FADX 15 Index - January 2026')
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate percentage changes
data['Percentage Change'] = data['Close'].pct_change() * 100

# Identify significant changes (> 2%)
significant_changes = data[abs(data['Percentage Change']) > 2]
print("Significant changes:")
print(significant_changes)

# Save significant changes to a new CSV
significant_changes.to_csv('Significant_Changes.csv', index=False)
