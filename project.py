import pandas as pd
import matplotlib.pyplot as plt

data_csv = "gym_sensor_data_2023-04-02_to_2023-04-09.csv"

# Use comma as the delimiter since your CSV is comma-separated
data = pd.read_csv(data_csv)

print(data.head(n=10))

# Assuming 'timestamp' column needs to be parsed as datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Now you can plot your data
data.plot(x="timestamp", y="machine_1", title="Machine 1 Usage Over Time")
plt.show()