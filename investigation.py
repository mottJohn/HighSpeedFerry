import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import hsf as hsf#for filtering zones
data = pd.read_csv('18-DEC-2018.csv')

#filtered zone
data['enteredZone'] = data.apply(lambda row: hsf.enteredZone(row['Latitude'], row['Longitude']), axis = 1)
data['Local Time'] = pd.to_datetime(data['Local Time'], errors='coerce')

#filter time
dt_start = datetime(2018, 12, 18, 17, 3, 52)
dt_end = datetime(2018,12,18,17,31,45)
withinZoneTime_data = data[(data['Local Time'] >= dt_start)  & (data['Local Time' ] <= dt_end) & data['enteredZone'] == True]
print(len(withinZoneTime_data['MMIS'].unique()))
withinZoneTime_data.to_csv('filtered.csv')


groupby_ship = withinZoneTime_data.groupby('Vessel Name')


for name, group in groupby_ship:
    plt.scatter(group['Longitude'], group['Latitude'], label = name)
plt.legend()
plt.show()

for name, group in groupby_ship:
    plt.plot(group['Local Time'], group['Latitude'], label = name)
plt.legend()
plt.show()