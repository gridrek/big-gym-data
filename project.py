import pandas as pd
import matplotlib.pyplot as plt

data_csv = "gym_sensor_data_2023-04-02_to_2023-04-09.csv"

data = pd.read_csv("./" + data_csv, sep=";", skiprows=0)

print(data.head(n=10))

data.plot(x="timestamp", y="machine_1", title="usage") #det här funkar inte för fan