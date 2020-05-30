import requests
from datetime import datetime
import time
import numpy as np
import csv


def dane(currency, start_date):
    now = datetime.now()
    unixtime_now = int(time.mktime(now.timetuple()))
    time_difference = unixtime_now - start_date
    nr_of_results = int(time_difference / (60 * 60 * 24))
    link = "https://www.bitstamp.net/api/v2/ohlc/" + currency + "usd/"
    bitstamp = requests.get(link,
                            params={"step": 86400, "limit": nr_of_results, "start": start_date, "end": unixtime_now})
    bitstamp = bitstamp.json()
    bitstamp = bitstamp['data']['ohlc']
    timestamps = []
    volumes = []
    for i in bitstamp:
        timestamps.append(int(i['timestamp']))
        volumes.append(float(i['volume']))

    dates = []
    for j in timestamps:
        dates.append(datetime.fromtimestamp(j))

    zmiana_dzienna_proc = []
    for k in range(len(volumes) - 1):
        zmiana_dzienna_proc.append(round(((volumes[k + 1] / volumes[k]) - 1) * 100, 2))

    zmiana_rodzaj = []
    for i in zmiana_dzienna_proc:
        if i > 0:
            zmiana_rodzaj.append(1)
        else:
            zmiana_rodzaj.append(0)

    return volumes, timestamps, dates, zmiana_dzienna_proc, zmiana_rodzaj, nr_of_results


def zmiana_rodzaj_probability(currency, start_date):
    _, _, _, zmiana_dzienna_proc, zmiana_rodzaj, _ = dane(currency, start_date)
    x = []
    y = []
    for i in range(len(zmiana_rodzaj) - 2):
        x.append([zmiana_rodzaj[i], zmiana_rodzaj[i + 1]])
        y.append(zmiana_rodzaj[i + 2])

    x00_1 = 0
    x00_0 = 0
    x00 = 0
    x01_1 = 0
    x01_0 = 0
    x01 = 0
    x10_1 = 0
    x10_0 = 0
    x10 = 0
    x11_1 = 0
    x11_0 = 0
    x11 = 0

    y00_1 = []
    y00_0 = []

    y01_1 = []
    y01_0 = []

    y10_1 = []
    y10_0 = []

    y11_1 = []
    y11_0 = []

    for i in range(len(x)):
        if x[i] == [0, 0]:
            x00 += 1
            if y[i] == 1:
                x00_1 += 1
                y00_1.append(zmiana_dzienna_proc[i + 2])
            else:
                x00_0 += 1
                y00_0.append(zmiana_dzienna_proc[i + 2])
        elif x[i] == [0, 1]:
            x01 += 1
            if y[i] == 1:
                x01_1 += 1
                y01_1.append(zmiana_dzienna_proc[i + 2])
            else:
                x01_0 += 1
                y01_0.append(zmiana_dzienna_proc[i + 2])
        elif x[i] == [1, 0]:
            x10 += 1
            if y[i] == 1:
                x10_1 += 1
                y10_1.append(zmiana_dzienna_proc[i + 2])
            else:
                x10_0 += 1
                y10_0.append(zmiana_dzienna_proc[i + 2])
        elif x[i] == [1, 1]:
            x11 += 1
            if y[i] == 1:
                x11_1 += 1
                y11_1.append(zmiana_dzienna_proc[i + 2])
            else:
                x11_0 += 1
                y11_0.append(zmiana_dzienna_proc[i + 2])

    if x00 == 0:
        p_x00_1 = 0.5
        p_x00_0 = 0.5
    else:
        p_x00_1 = round(x00_1 / x00, 4)
        p_x00_0 = round(x00_0 / x00, 4)

    if x01 == 0:
        p_x01_1 = 0.5
        p_x01_0 = 0.5
    else:
        p_x01_1 = round(x01_1 / x01, 4)
        p_x01_0 = round(x01_0 / x01, 4)

    if x10 == 0:
        p_x10_1 = 0.5
        p_x10_0 = 0.5
    else:
        p_x10_1 = round(x10_1 / x10, 4)
        p_x10_0 = round(x10_0 / x10, 4)

    if x11 == 0:
        p_x11_1 = 0.5
        p_x11_0 = 0.5
    else:
        p_x11_1 = round(x11_1 / x11, 4)
        p_x11_0 = round(x11_0 / x11, 4)

    return p_x00_0, p_x00_1, p_x01_0, p_x01_1, p_x10_0, p_x10_1, p_x11_0, p_x11_1, y00_0, y00_1, y01_0, y01_1, \
           y10_0, y10_1, y11_0, y11_1


def predict_change(currency, start_date):
    p_x00_0, p_x00_1, p_x01_0, p_x01_1, p_x10_0, p_x10_1, p_x11_0, p_x11_1, y00_0, y00_1, y01_0, y01_1, y10_0, y10_1,\
        y11_0, y11_1 = zmiana_rodzaj_probability(currency, start_date)
    _, _, _, zmiana_dzienna_proc, zmiana_rodzaj, nr_of_results = dane(currency, start_date)

    new_zmiana_rodzaj = zmiana_rodzaj[-2:]
    new_zmiana_dzienna_proc = zmiana_dzienna_proc[-2:]
    for i in range(nr_of_results):
        if new_zmiana_rodzaj[-2] == 0 and new_zmiana_rodzaj[-1] == 0:
            a = np.random.choice([0, 1], p=[p_x00_0, p_x00_1])
            new_zmiana_rodzaj.append(a)
            if a == 0:
                new_percent_change = np.random.uniform(np.mean(y00_0) - (np.mean(y00_0) / 2),
                                                       np.mean(y00_0) + (np.mean(y00_0) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
            else:
                new_percent_change = np.random.uniform(np.mean(y00_1) - (np.mean(y00_1) / 2),
                                                       np.mean(y00_1) + (np.mean(y00_1) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
        elif new_zmiana_rodzaj[-2] == 0 and new_zmiana_rodzaj[-1] == 1:
            a = np.random.choice([0, 1], p=[p_x01_0, p_x01_1])
            new_zmiana_rodzaj.append(a)
            if a == 0:
                new_percent_change = np.random.uniform(np.mean(y01_0) - (np.mean(y01_0) / 2),
                                                       np.mean(y01_0) + (np.mean(y01_0) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
            else:
                new_percent_change = np.random.uniform(np.mean(y01_1) - (np.mean(y01_1) / 2),
                                                       np.mean(y01_1) + (np.mean(y01_1) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
        elif new_zmiana_rodzaj[-2] == 1 and new_zmiana_rodzaj[-1] == 0:
            a = np.random.choice([0, 1], p=[p_x10_0, p_x10_1])
            new_zmiana_rodzaj.append(a)
            if a == 0:
                new_percent_change = np.random.uniform(np.mean(y10_0) - (np.mean(y10_0) / 2),
                                                       np.mean(y10_0) + (np.mean(y10_0) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
            else:
                new_percent_change = np.random.uniform(np.mean(y10_1) - (np.mean(y10_1) / 2),
                                                       np.mean(y10_1) + (np.mean(y10_1) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
        elif new_zmiana_rodzaj[-2] == 1 and new_zmiana_rodzaj[-1] == 1:
            a = np.random.choice([0, 1], p=[p_x11_0, p_x11_1])
            new_zmiana_rodzaj.append(a)
            if a == 0:
                new_percent_change = np.random.uniform(np.mean(y11_0) - (np.mean(y11_0) / 2),
                                                       np.mean(y11_0) + (np.mean(y11_0) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)
            else:
                new_percent_change = np.random.uniform(np.mean(y11_1) - (np.mean(y11_1) / 2),
                                                       np.mean(y11_1) + (np.mean(y11_1) / 2))
                new_percent_change = round(new_percent_change, 4)
                new_zmiana_dzienna_proc.append(new_percent_change)

    return new_zmiana_rodzaj[2:], new_zmiana_dzienna_proc[2:]


def predict_volume(currency, date):
    _, new_zmiana_dzienna_proc = predict_change(currency, date)
    volumes, timestamps, _, _, _, nr_of_results = dane(currency, date)
    new_volumes = [volumes[-1]]
    new_timestamps = [timestamps[-1]]
    average_volumes = np.average(volumes)
    for i in range(len(new_zmiana_dzienna_proc)):
        new_zmiana_dzienna_proc[i] = round(new_zmiana_dzienna_proc[i]/100, 4)

    for i in range(nr_of_results):
        new_volumes.append(average_volumes + (average_volumes * new_zmiana_dzienna_proc[i]))
        new_timestamps.append(new_timestamps[i] + (60*60*24))
    return new_volumes, new_timestamps

#dostępne waluty: btc, xrp, ltc
#czas max 1000 dni wstecz

waluta = 'btc'
czas = 1580338800

volumes, timestamps, _, _, _, _ = dane(waluta, czas)
new_volumes, new_timestamps = predict_volume(waluta, czas)

new_volumes_list = []

for i in range(100):
    new_volumes, _ = predict_volume(waluta, czas)
    new_volumes_list.append(new_volumes)

new_volumes_transposed = np.transpose(new_volumes_list)
new_volumes_average = np.average(new_volumes_transposed, 1)
new_volumes_median = np.median(new_volumes_transposed, 1)
new_volumes_std = np.std(new_volumes_transposed, 1)

f = open('new_volumes_1_simulation.csv', 'w')
with f:
    fnames = ['timestamp', 'volume']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    for i in range(len(new_volumes)):
        writer.writerow({'timestamp': new_timestamps[i], 'volume': new_volumes[i]})

f = open('new_volumes_100_simulations.csv', 'w')
with f:
    fnames = ['timestamp', 'volume', 'median', 'std']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    for i in range(len(new_volumes)):
        writer.writerow({'timestamp': new_timestamps[i], 'volume': new_volumes_average[i],
                         'median': new_volumes_median[i], 'std': new_volumes_std[i]})

f = open('old_volumes.csv', 'w')
with f:
    fnames = ['timestamp', 'volume']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    for i in range(len(volumes)):
        writer.writerow({'timestamp': timestamps[i], 'volume': volumes[i]})
