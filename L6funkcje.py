from tkinter import simpledialog
import csv
from datetime import datetime
import requests
from tkinter import *
import time

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


def bitstamp_trades():
    response1 = requests.get("https://www.bitstamp.net/api/v2/transactions/btcusd", params={"time": 'day'})
    response2 = requests.get("https://www.bitstamp.net/api/v2/transactions/xrpusd", params={"time": 'day'})
    response3 = requests.get("https://www.bitstamp.net/api/v2/transactions/ltcusd", params={"time": 'day'})
    response4 = requests.get("https://www.bitstamp.net/api/v2/transactions/ethusd", params={"time": 'day'})
    response5 = requests.get("https://www.bitstamp.net/api/v2/transactions/bchusd", params={"time": 'day'})
    btc_data = response1.json()
    xrp_data = response2.json()
    ltc_data = response3.json()
    eth_data = response4.json()
    bch_data = response5.json()
    return btc_data, xrp_data, ltc_data, eth_data, bch_data


def currency_current_price():
    btc, xrp, ltc, eth, bch = bitstamp_ticker()
    btc_last = float(btc['last'])
    xrp_last = float(xrp['last'])
    ltc_last = float(ltc['last'])
    eth_last = float(eth['last'])
    bch_last = float(bch['last'])
    return btc_last, xrp_last, ltc_last, eth_last, bch_last


def bitstamp_gain(hour, minute):

    now = datetime.now()
    unixtime_now = time.mktime(now.timetuple())
    t = unixtime_now - (hour * 60 * 60) - (minute * 60)

    btc, xrp, ltc, eth, bch = bitstamp_trades()

    btc_0 = []
    xrp_0 = []
    ltc_0 = []
    eth_0 = []
    bch_0 = []

    btc_1 = []
    xrp_1 = []
    ltc_1 = []
    eth_1 = []
    bch_1 = []
    for i in range(len(btc)):
        if btc[i]['type'] == '0':
            btc_0.append(btc[i])
        else:
            btc_1.append(btc[i])

    for i in range(len(xrp)):
        if xrp[i]['type'] == '0':
            xrp_0.append(xrp[i])
        else:
            xrp_1.append(xrp[i])

    for i in range(len(ltc)):
        if ltc[i]['type'] == '0':
            ltc_0.append(ltc[i])
        else:
            ltc_1.append(ltc[i])

    for i in range(len(eth)):
        if eth[i]['type'] == '0':
            eth_0.append(eth[i])
        else:
            eth_1.append(eth[i])

    for i in range(len(bch)):
        if bch[i]['type'] == '0':
            bch_0.append(bch[i])
        else:
            bch_1.append(bch[i])

    btc_now = btc_1[0]['price']
    xrp_now = xrp_1[0]['price']
    ltc_now = ltc_1[0]['price']
    eth_now = eth_1[0]['price']
    bch_now = bch_1[0]['price']

    btc_then = 0
    xrp_then = 0
    ltc_then = 0
    eth_then = 0
    bch_then = 0

    for i in range(len(btc_1)):
        if int(btc_1[i]['date']) >= t:
            btc_then = btc_1[i]['price']

    for i in range(len(xrp_1)):
        if int(xrp_1[i]['date']) >= t:
            xrp_then = xrp_1[i]['price']

    for i in range(len(ltc_1)):
        if int(ltc_1[i]['date']) >= t:
            ltc_then = ltc_1[i]['price']

    for i in range(len(eth_1)):
        if int(eth_1[i]['date']) >= t:
            eth_then = eth_1[i]['price']

    for i in range(len(bch_1)):
        if int(bch_1[i]['date']) >= t:
            bch_then = bch_1[i]['price']

    btc_now = float(btc_now)
    xrp_now = float(xrp_now)
    ltc_now = float(ltc_now)
    eth_now = float(eth_now)
    bch_now = float(bch_now)

    btc_then = float(btc_then)
    xrp_then = float(xrp_then)
    ltc_then = float(ltc_then)
    eth_then = float(eth_then)
    bch_then = float(bch_then)

    btc_g_percent = round(((btc_now-btc_then)/btc_then) * 100, 2)
    xrp_g_percent = round(((xrp_now-xrp_then)/xrp_then) * 100, 2)
    ltc_g_percent = round(((ltc_now-ltc_then)/ltc_then) * 100, 2)
    eth_g_percent = round(((eth_now-eth_then)/eth_then) * 100, 2)
    bch_g_percent = round(((bch_now-bch_then)/bch_then) * 100, 2)

    btc_g = round(btc_now - btc_then, 2)
    xrp_g = round(xrp_now - xrp_then, 5)
    ltc_g = round(ltc_now - ltc_then, 2)
    eth_g = round(eth_now - eth_then, 2)
    bch_g = round(bch_now - bch_then, 2)

    btc = [btc_now, btc_then, btc_g, btc_g_percent]
    xrp = [xrp_now, xrp_then, xrp_g, xrp_g_percent]
    ltc = [ltc_now, ltc_then, ltc_g, ltc_g_percent]
    eth = [eth_now, eth_then, eth_g, eth_g_percent]
    bch = [bch_now, bch_then, bch_g, bch_g_percent]

    date_now = datetime.fromtimestamp(unixtime_now)
    date_then = datetime.fromtimestamp(t)

    return btc, xrp, ltc, eth, bch, date_now, date_then

########################################################################################################################
def add_btc(a):
    amount = simpledialog.askfloat("DODAJ BTC", "Ile btc chesz dodać?", parent=a, minvalue=0.0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '+'
    if amount is not None:
        f = open('btc.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date' : now, 'sign': sign, 'amount': amount})


def del_btc(a):
    amount = simpledialog.askfloat("USUN BTC", "Ile btc chesz usunąć?", parent=a, minvalue=0.0, maxvalue=suma_btc())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '-'
    if amount is not None:
        f = open('btc.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date' : now, 'sign': sign, 'amount': amount})


def suma_btc():
    f = open('btc.csv', 'r')
    a = []
    znak = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            a.append(float(row['amount']))
            znak.append(row['sign'])

    for i in range(len(a)):
        if znak[i] == '-':
            a[i] = -a[i]
    return sum(a)
########################################################################################################################
def add_xrp(a):
    amount = simpledialog.askfloat("DODAJ XRP", "Ile xrp chesz dodać?", parent=a, minvalue=0.0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '+'
    if amount is not None:
        f = open('xrp.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date' : now, 'sign': sign, 'amount': amount})


def del_xrp(a):
    amount = simpledialog.askfloat("USUN XRP", "Ile xrp chesz usunąć?", parent=a, minvalue=0.0, maxvalue=suma_xrp())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '-'
    if amount is not None:
        f = open('xrp.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date' : now, 'sign': sign, 'amount': amount})


def suma_xrp():
    f = open('xrp.csv', 'r')
    a = []
    znak = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            a.append(float(row['amount']))
            znak.append(row['sign'])

    for i in range(len(a)):
        if znak[i] == '-':
            a[i] = -a[i]
    return sum(a)
########################################################################################################################
def add_ltc(a):
    amount = simpledialog.askfloat("DODAJ LTC", "Ile LTC chesz dodać?", parent=a, minvalue=0.0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '+'
    if amount is not None:
        f = open('ltc.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def del_ltc(a):
    amount = simpledialog.askfloat("USUN LTC", "Ile ltc chesz usunąć?", parent=a, minvalue=0.0, maxvalue=suma_ltc())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '-'
    if amount is not None:
        f = open('ltc.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def suma_ltc():
    f = open('ltc.csv', 'r')
    a = []
    znak = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            a.append(float(row['amount']))
            znak.append(row['sign'])

    for i in range(len(a)):
        if znak[i] == '-':
            a[i] = -a[i]
    return sum(a)
########################################################################################################################
def add_eth(a):
    amount = simpledialog.askfloat("DODAJ ETH", "Ile ETH chesz dodać?", parent=a, minvalue=0.0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '+'
    if amount is not None:
        f = open('eth.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def del_eth(a):
    amount = simpledialog.askfloat("USUN ETH", "Ile eth chesz usunąć?", parent=a, minvalue=0.0, maxvalue=suma_eth())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '-'
    if amount is not None:
        f = open('eth.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def suma_eth():
    f = open('eth.csv', 'r')
    a = []
    znak = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            a.append(float(row['amount']))
            znak.append(row['sign'])

    for i in range(len(a)):
        if znak[i] == '-':
            a[i] = -a[i]
    return sum(a)
########################################################################################################################
def add_bch(a):
    amount = simpledialog.askfloat("DODAJ BCH", "Ile bch chesz dodać?", parent=a, minvalue=0.0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '+'
    if amount is not None:
        f = open('bch.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def del_bch(a):
    amount = simpledialog.askfloat("USUN BCH", "Ile bch chesz usunąć?", parent=a, minvalue=0.0, maxvalue=suma_bch())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = '-'
    if amount is not None:
        f = open('bch.csv', 'a')
        with f:
            fnames = ['date', 'sign', 'amount']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writerow({'date': now, 'sign': sign, 'amount': amount})


def suma_bch():
    f = open('bch.csv', 'r')
    a = []
    znak = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            a.append(float(row['amount']))
            znak.append(row['sign'])

    for i in range(len(a)):
        if znak[i] == '-':
            a[i] = -a[i]
    return sum(a)
########################################################################################################################
def get_history(a):
    if a == 'btc':
        f = open('btc.csv', 'r')
    elif a == 'xrp':
        f = open('xrp.csv', 'r')
    elif a == 'ltc':
        f = open('ltc.csv', 'r')
    elif a == 'eth':
        f = open('eth.csv', 'r')
    elif a == 'bch':
        f = open('bch.csv', 'r')
    hist = []
    with f:
        fnames = ['date', 'sign', 'amount']
        reader = csv.DictReader(f, fieldnames=fnames)
        for row in reader:
            hist.append("data: " + row['date'] + "\twartość: " + row['sign'] + row['amount'])
    return hist


def set_history(options, txt):
    hist = get_history(options.get())
    txt.config(state='normal')
    txt.delete(1.0, END)
    for x in hist:
        txt.insert(END, x + "\n")
    txt.config(state='disabled')


def frame_check(frame,check,r):
    if check == 0:
        frame.grid_forget()
    if check == 1:
        frame.grid(row=r)
