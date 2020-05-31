import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

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

f = open('real_volumes.csv', 'r')

real_volumes = []
real_timestamps = []
with f:
    reader = csv.DictReader(f)
    for row in reader:
        real_volumes.append(float(row['volume']))
        real_timestamps.append(int(row['timestamp']))

old_dates = []
for j in timestamps:
    old_dates.append(datetime.fromtimestamp(j))

new_dates = []
for j in new_timestamps:
    new_dates.append(datetime.fromtimestamp(j))

real_dates = []
for j in real_timestamps:
    real_dates.append(datetime.fromtimestamp(j))


plt.figure(1)
plt.plot(old_dates, volumes, 'b', label='Old volumes')
plt.plot(real_dates, real_volumes, 'b')
plt.plot(new_dates, volumes_single_simulation, 'r', label='Single simulation volumes')
plt.plot(new_dates, volumes_multiple_simulation, 'g', label='100 simulations average volumes')
plt.legend(loc='best')
plt.xlabel('date')
plt.ylabel('volume')
plt.title("Daily volume simulation")
plt.grid()

plt.figure(2)
plt.plot(real_dates, real_volumes, 'b', label='Real data')
plt.plot(new_dates, volumes_single_simulation, 'r', label='Single simulation volumes')
plt.plot(new_dates, volumes_multiple_simulation, 'g', label='100 simulations average volumes')
plt.legend(loc='best')
plt.xlabel('date')
plt.ylabel('volume')
plt.title("Daily volume simulation")
plt.grid()


diff_1 = []
diff_100 = []
for i in range(len(real_volumes)):
    diff_1.append(np.abs(real_volumes[i]-volumes_single_simulation[i]))
    diff_100.append(np.abs(real_volumes[i]-volumes_multiple_simulation[i]))

plt.figure(3)
x = range(len(diff_1))
plt.plot(x, diff_1, 'r', label='1 simulation')
plt.plot(x, diff_100, 'b', label='100 simulation average')
plt.legend(loc='best')
plt.title('Difference between real data and simulations')
plt.grid()
plt.show()

diff_1_sum = sum(diff_1)
diff_100_sum = sum(diff_100)

diff_1_avg = np.average(diff_1)
diff_100_avg = np.average(diff_100)

diff_1_median = np.median(diff_1)
diff_100_median = np.median(diff_100)

diff_1_std = np.std(diff_1)
diff_100_std = np.std(diff_100)

print("Suma różnic:")
print("\tPojedyńcza symulacja:", diff_1_sum)
print("\t100 symulacji:       ", diff_100_sum)
print("Średnia dzienna różnica:")
print("\tPojedyńcza symulacja:", diff_1_avg)
print("\t100 symulacji:       ", diff_100_avg)
print("Mediana różnic:")
print("\tPojedyńcza symulacja:", diff_1_median)
print("\t100 symulacji:       ", diff_100_median)
print("Odchylenie standardowe różnic:")
print("\tPojedyńcza symulacja:", diff_1_std)
print("\t100 symulacji:       ", diff_100_std)
