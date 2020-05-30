import csv
import matplotlib.pyplot as plt
from datetime import datetime


f = open('new_volumes_1_simulation.csv', 'r')

volumes_single_simulation = []
new_timestamps = []
with f:
    reader = csv.DictReader(f)
    for row in reader:
        volumes_single_simulation.append(float(row['volume']))
        new_timestamps.append(int(row['timestamp']))

f = open('new_volumes_100_simulations.csv', 'r')

volumes_multiple_simulation = []
simulations_median = []
simulations_std = []
with f:
    reader = csv.DictReader(f)
    for row in reader:
        volumes_multiple_simulation.append(float(row['volume']))
        simulations_median.append(float(row['median']))
        simulations_std.append(float(row['std']))


f = open('old_volumes.csv', 'r')
volumes = []
timestamps = []
with f:
    reader = csv.DictReader(f)
    for row in reader:
        volumes.append(float(row['volume']))
        timestamps.append(int(row['timestamp']))

old_dates = []
for j in timestamps:
    old_dates.append(datetime.fromtimestamp(j))
new_dates = []

for j in new_timestamps:
    new_dates.append(datetime.fromtimestamp(j))

plt.figure(1)
plt.plot(old_dates, volumes, 'b', label='Old volumes')
plt.plot(new_dates, volumes_single_simulation, 'r', label='Single simulation volumes')
plt.plot(new_dates, volumes_multiple_simulation, 'g', label='100 simulations average volumes')
plt.legend(loc='best')
plt.xlabel('date')
plt.ylabel('volume')
plt.title("Daily volume simulation")
plt.grid()

plt.figure(2)
x = range(len(simulations_median))
plt.plot(x[1:], simulations_median[1:], label='daily medians')
plt.plot(x[1:], volumes_multiple_simulation[1:], label='daily average')
plt.legend(loc='best')
plt.ylabel('volume')
plt.xlabel('next days')
plt.title("100 volume simulations")
plt.grid()

plt.figure(3)
plt.plot(x[1:], simulations_std[1:], label='standard deviation')
plt.legend(loc='best')
plt.xlabel('next days')
plt.title("100 volume simulations")
plt.grid()

plt.show()
