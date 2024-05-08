import pandas as pd
from matplotlib import pyplot as plt

# Load the CSV data
data_csv = "gym_sensor_data_2023-04-02_to_2023-04-09.csv"
data = pd.read_csv(data_csv)

# Convert 'timestamp' column to datetime and set as index
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# Define a threshold for active usage
active_usage_threshold = 50

# Create a new column to represent active usage (1 if machine_1 is in use, 0 otherwise)
data['machine_1_active'] = (data['machine_1'] > active_usage_threshold).astype(int)

# Resample by hour and sum up the counts of active usage points
data_resampled = data.resample('H').sum()

# Display the first few rows of the hourly resampled data
print(data_resampled.head(n=10))

# Plot the data for the number of minutes machine_1 was in active use per hour
data_resampled.plot(y='machine_1_active', title='Machine 1 Active Usage per Hour')
plt.xlabel('Time (hours)')
plt.ylabel('Active Usage Count (per hour)')
plt.show()
