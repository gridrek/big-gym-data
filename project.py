import pandas as pd
from matplotlib import pyplot as plt

data_csv = "gym_sensor_data_2023-04-02_to_2023-04-09.csv"

# Read the CSV data
data = pd.read_csv(data_csv)

# Convert 'timestamp' column to datetime and set it as the index
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# Resample data by hour and aggregate using sum
data_resampled = data.resample('H').sum()

# Display the first few rows of the hourly resampled data
print(data_resampled.head(n=10))

# Plot resampled data (example with machine_1)
data_resampled.plot(y='machine_1', title='Machine 1 Usage per Hour')
plt.xlabel('Time (hours)')
plt.ylabel('Usage')
plt.show()
