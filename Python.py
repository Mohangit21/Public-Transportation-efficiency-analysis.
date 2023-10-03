import pandas as pd
import matplotlib.pyplot as plt

# Sample Data: Replace this with your actual data or use APIs to fetch real-time data
# For simplicity, I'm creating a DataFrame with hypothetical data.
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Ridership': [1200, 1250, 1300, 1100, 1400, 1500, 1600, 1550, 1650, 1700, 1800, 1750, 2000, 2100, 2200, 2150, 2300, 2400, 2350, 2500, 2600, 2700, 2650, 2800, 2900, 3000, 2950, 3100, 3200, 3150, 3300],
    'On-Time_Percentage': [90, 92, 88, 94, 91, 93, 89, 95, 92, 90, 93, 91, 96, 94, 92, 97, 93, 91, 95, 92, 90, 94, 91, 98, 96, 93, 91, 95, 92, 90, 94],
}

df = pd.DataFrame(data)

# Basic Analysis
avg_ridership = df['Ridership'].mean()
on_time_avg = df['On-Time_Percentage'].mean()

# Visualizations
plt.figure(figsize=(10, 6))

# Ridership Over Time
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['Ridership'], marker='o', linestyle='-', color='b')
plt.title('Ridership Over Time')
plt.xlabel('Date')
plt.ylabel('Ridership')

# On-Time Percentage Over Time
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['On-Time_Percentage'], marker='o', linestyle='-', color='g')
plt.title('On-Time Percentage Over Time')
plt.xlabel('Date')
plt.ylabel('On-Time Percentage')

plt.tight_layout()
plt.show()

# Print Results
print(f'Average Ridership: {avg_ridership:.2f}')
print(f'Average On-Time Percentage: {on_time_avg:.2f}%')
