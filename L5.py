import requests
import time


def bubble(a):
    tab_size = len(a)
    tab = a.copy()
    ind = list(range(tab_size))
    w = 1
    while w != (tab_size-1):
        w = tab_size - 1
        for i in range(tab_size-1):
            if tab[i] < tab[i + 1]:
                w = w - 1
                b1 = tab[i]
                b2 = tab[i + 1]
                tab[i] = b2
                tab[i + 1] = b1

                in1 = ind[i]
                in2 = ind[i + 1]
                ind[i] = in2
                ind[i + 1] = in1
    return tab, ind


def bitstamp_ticker():
    response1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
    response2 = requests.get("https://www.bitstamp.net/api/v2/ticker/xrpusd")
    response3 = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd")
    response4 = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd")
    response5 = requests.get("https://www.bitstamp.net/api/v2/ticker/bchusd")
    btc_data = response1.json()
    xrp_data = response2.json()
    ltc_data = response3.json()
    eth_data = response4.json()
    bch_data = response5.json()
    return btc_data, xrp_data, ltc_data, eth_data, bch_data


def funkcja():
    btc, xrp, ltc, eth, bch = bitstamp_ticker()

    btc_high = float(btc["high"])
    btc_low = float(btc["low"])

    xrp_high = float(xrp["high"])
    xrp_low = float(xrp["low"])

    ltc_high = float(ltc["high"])
    ltc_low = float(ltc["low"])

    eth_high = float(eth["high"])
    eth_low = float(eth["low"])

    bch_high = float(bch["high"])
    bch_low = float(bch["low"])

    gain = [(btc_high / btc_low - 1) * 100, (xrp_high / xrp_low - 1) * 100, (ltc_high / ltc_low - 1) * 100,
            (eth_high / eth_low - 1) * 100, (bch_high / bch_low - 1) * 100]

    names = ["BTC", "XRP", "LTC", "ETH", "BCH"]

    for i in range(len(gain)):
        gain[i] = round(gain[i], 2)

    gain_sorted, ind = bubble(gain)
    names_sorted = []
    for i in range(len(ind)):
        names_sorted.append(names[ind[i]])

    for i in range(len(gain_sorted)):
        if gain_sorted[i] > 0:
            print(names_sorted[i], " +", gain_sorted[i])
        else:
            print(names_sorted[i], " ",gain_sorted[i] )


while 1:
    funkcja()
    time.sleep(300)
