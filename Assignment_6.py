# Load the Libraries
#Libraries for Data Manipulation
import os
import pandas as pd
import numpy as np

# Libraries for Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample data instead of loading from file
# This is the same data that was shown in your original example
data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 45, 30, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, 375.8, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, 375.8, 280.0, 380.3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Fill any missing values with mean for numeric columns
for col in ['Duration', 'Pulse', 'Maxpulse', 'Calories']:
    df[col].fillna(df[col].mean(), inplace=True)

# Histogram of 'Duration'
# Set up the figure size
plt.figure(figsize=(15, 10))

# Histogram of 'Duration'
plt.subplot(2, 2, 1)
sns.histplot(df['Duration'], bins=30, kde=True)
plt.title('Duration Distribution')
# Histogram of 'Pulse'
plt.subplot(2, 2, 2)
sns.histplot(df['Pulse'], bins=30, kde=True)
plt.title('Pulse Distribution')

# Histogram of 'Maxpulse'
plt.subplot(2, 2, 3)
sns.histplot(df['Maxpulse'], bins=30, kde=True)
plt.title('Maxpulse Distribution')

# Histogram of 'Calories'
plt.subplot(2, 2, 4)
sns.histplot(df['Calories'], bins=30, kde=True)
plt.title('Calories Distribution')

# Display the plot
plt.tight_layout()
plt.show()