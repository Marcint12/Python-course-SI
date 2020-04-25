import requests


def bitstamp_sell_buy():
    response = requests.get("https://www.bitstamp.net/api/order_book/")
    data = response.json()
    bids = data["bids"]
    asks = data["asks"]
    print("Bids and asks from www.bitstamp.net:\n")
    print("List of purchase orders:\n")
    print(bids, "\n")
    print("List of sell orders:\n")
    print(asks)


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


def compare_bids_asks_bitstamp_cex():
    bitstamp_bid, bitstamp_ask = bitstamp_ticker()
    cex_bid, cex_ask = cex_ticker()
    print("\n\nBTC/USD exchange comparsion on bitstamp.net and cex.io:\n")
    print("Highest purchase order on bitstamp: ", bitstamp_bid, " , lowest sell order on bitstamp: ", bitstamp_ask)
    print("\nHighest purchase order on cex: ", cex_bid, " , lowest sell order on cex: ", cex_ask)

    bitstamp_ask = float(bitstamp_ask)
    bitstamp_bid = float(bitstamp_bid)
    cex_ask = float(cex_ask)
    cex_bid = float(cex_bid)

    bid_diff = abs(bitstamp_bid - cex_bid)
    ask_diff = abs(bitstamp_ask - cex_ask)
    bid_diff = round(bid_diff, 2)
    ask_diff = round(ask_diff, 2)

    if bitstamp_bid > cex_bid:
        print("\nIt is more profitable to sell BTC on bitstamp.net. You will earn: ", bid_diff, "USD more.")
    elif cex_bid > bitstamp_bid:
        print("\nIt is more profitable to sell BTC on cex.io. You will earn: ", bid_diff, "USD more.")
    else:
        print("You can sell BTC for the same price on bitstamp.net and cex.io")

    if bitstamp_ask < cex_ask:
        print("\nBTC is cheaper on bitstamp.net. You will save ", ask_diff, "USD.")
    elif cex_ask < bitstamp_ask:
        print("\nBTC is cheaper on cex.io. You will save ", ask_diff, "USD.")
    else:
        print("You can buy BTC for the same price on bitstamp.net and cex.io")


bitstamp_sell_buy()
compare_bids_asks_bitstamp_cex()
