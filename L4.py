import requests
import time


def bitstamp_ticker():
    response = requests.get("https://www.bitstamp.net/api/ticker/")
    data = response.json()
    highest_bid = data["bid"]
    lowest_ask = data["ask"]
    return highest_bid, lowest_ask


def cex_ticker():
    response = requests.get("https://cex.io/api/ticker/BTC/USD")
    data = response.json()
    highest_bid = data["bid"]
    lowest_ask = data["ask"]
    return highest_bid, lowest_ask


def coinbase_ticker():
    response1 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell")
    response2 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
    data1 = response1.json()
    data2 = response2.json()
    highest_bid = data1["data"]["amount"]
    lowest_ask = data2["data"]["amount"]
    return highest_bid, lowest_ask


def bitbay_ticker():
    response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
    data = response.json()
    highest_bid = data["bid"]
    lowest_ask = data["ask"]
    return highest_bid, lowest_ask


def compare_prices():
    bid_bitstamp, ask_bitstamp = bitstamp_ticker()
    bid_cex, ask_cex = cex_ticker()
    bid_coinbase, ask_coinbase = coinbase_ticker()
    bid_bitbay, ask_bitbay = bitbay_ticker()

    bid_bitstamp = float(bid_bitstamp)
    ask_bitstamp = float(ask_bitstamp)
    bid_cex = float(bid_cex)
    ask_cex = float(ask_cex)
    bid_coinbase = float(bid_coinbase)
    ask_coinbase = float(ask_coinbase)
    bid_bitbay = float(bid_bitbay)
    ask_bitbay = float(ask_bitbay)

    bids = [bid_bitbay, bid_coinbase, bid_bitstamp, bid_cex]
    asks = [ask_bitbay, ask_coinbase, ask_bitstamp, ask_cex]
    volume = 0.1

    # fees depend on your trading volume in the last 30 days
    fee_bitstamp = 0.005
    fee_cex = 0.0025
    fee_coinbase = 0.005
    fee_bitbay = 0.0043

    bid_bitstamp = bid_bitstamp * volume - (bid_bitstamp * fee_bitstamp * volume)
    ask_bitstamp = ask_bitstamp * volume + (ask_bitstamp * fee_bitstamp * volume)
    bid_cex = bid_cex * volume - (bid_cex * fee_cex * volume)
    ask_cex = ask_cex * volume + (ask_cex * fee_cex * volume)
    bid_coinbase = bid_coinbase * volume - (bid_coinbase * fee_coinbase * volume)
    ask_coinbase = ask_coinbase * volume + (ask_coinbase * fee_coinbase * volume)
    bid_bitbay = bid_bitbay * volume - (bid_bitbay * fee_bitbay * volume)
    ask_bitbay = ask_bitbay * volume + (ask_bitbay * fee_bitbay * volume)

    bids_caluculated = [bid_bitbay, bid_coinbase, bid_bitstamp, bid_cex]
    asks_calculated = [ask_bitbay, ask_coinbase, ask_bitstamp, ask_cex]
    names = ["bitbay.net", "coinbase.com", "bitstamp.net", "cex.io"]

    b = bids_caluculated.index(max(bids_caluculated))
    a = asks_calculated.index(min(asks_calculated))

    diff = bids_caluculated[b] - asks_calculated[a]
    diff = round(diff, 2)

    if diff <= 0:
        print("\nArbitrage is not possible.")
        diff = 0
    else:
        print("\nArbitrage is possible.")
        print("You can buy ", volume, "BTC on ", names[a], "at the exchange rate of: ", asks[a], " USD, and sell "
                                                                                                 "it on", names[b],
              "at the exchange rate of ", bids[b], "USD. You will earn ", diff, "USD.")

    return diff


wallet = 0
number_of_operation = 0

while 1:
    number_of_operation = number_of_operation + 1
    print("\nOperation nr: ", number_of_operation)
    earnings = compare_prices()
    wallet = wallet + earnings
    wallet = round(wallet, 2)
    print("Executing transaction if possible.")
    print("\nYou have earned", wallet, "USD in total.")
    time.sleep(3)
