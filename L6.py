from tkinter import *
import L6funkcje
from tkinter import scrolledtext
from datetime import datetime

def wallet_window():
    def update_variables():
        global btc, xrp, ltc, eth, bch, time_now, time_then
        btc, xrp, ltc, eth, bch, time_now, time_then = L6funkcje.bitstamp_gain(hours.get(), minutes.get())

        global btc_last, xrp_last, ltc_last, eth_last, bch_last
        btc_last, xrp_last, ltc_last, eth_last, bch_last = L6funkcje.currency_current_price()

    window = Toplevel()
    window.title("Portfel")
    window.geometry('+0+0')

    top_frame = Frame(window)
    top_frame.grid(row=0)
    top_frame2 = Frame(window)
    top_frame2.grid(row=1)
    top_frame3 = Frame(window)
    top_frame3.grid(row=2)

    btc_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='BTC', font=("Arial", 15))
    L6funkcje.frame_check(btc_frame, btc_check.get(), 3)
    xrp_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='XRP', font=("Arial", 15))
    L6funkcje.frame_check(xrp_frame, xrp_check.get(), 4)
    eth_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='ETH', font=("Arial", 15))
    L6funkcje.frame_check(eth_frame, eth_check.get(), 5)
    ltc_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='LTC', font=("Arial", 15))
    L6funkcje.frame_check(ltc_frame, ltc_check.get(), 6)
    bch_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='BCH', font=("Arial", 15))
    L6funkcje.frame_check(bch_frame, bch_check.get(), 7)

    sum_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='RAZEM', font=("Arial", 15))
    sum_frame.grid(row=8)
    bottom_frame = Frame(window, padx=4, pady=4, bg='red')
    bottom_frame.grid(row=9)

    top_label = Label(top_frame, width=20, text="Dostępne waluty:", font=("Times New Roman", 10)
                      ).grid(row=0, column=0)
    btc_c = Checkbutton(top_frame, text="BTC", font=("Arial", 10), variable=btc_check,
                        command=lambda: L6funkcje.frame_check(btc_frame, btc_check.get(), 3)).grid(row=0, column=1)
    xrp_c = Checkbutton(top_frame, text="XRP", font=("Arial", 10), variable=xrp_check,
                        command=lambda: L6funkcje.frame_check(xrp_frame, xrp_check.get(), 4)).grid(row=0, column=2)
    eth_c = Checkbutton(top_frame, text="ETH", font=("Arial", 10), variable=eth_check,
                        command=lambda: L6funkcje.frame_check(eth_frame, eth_check.get(), 5)).grid(row=0, column=3)
    ltc_c = Checkbutton(top_frame, text="LTC", font=("Arial", 10), variable=ltc_check,
                        command=lambda: L6funkcje.frame_check(ltc_frame, ltc_check.get(), 6)).grid(row=0, column=4)
    bch_c = Checkbutton(top_frame, text="BCH", font=("Arial", 10), variable=bch_check,
                        command=lambda: L6funkcje.frame_check(bch_frame, bch_check.get(), 7)).grid(row=0, column=5)

    hours_list = []
    minutes_list = []
    for i in range(23):
        hours_list.append(i + 1)
    for i in range(61):
        if i % 5 == 0:
            minutes_list.append(i)

    top_label2 = Label(top_frame2, text="Zmień liczenie zmiany wartości na: ", font=("Times New Roman", 10)
                       ).grid(row=0, column=0)

    hours_change = OptionMenu(top_frame2, hours, *hours_list)
    hours_change.grid(row=0, column=1)

    hours_label = Label(top_frame2, text="h", font=("Times New Roman", 10)).grid(row=0, column=2)

    minutes_change = OptionMenu(top_frame2, minutes, *minutes_list)
    minutes_change.grid(row=0, column=3)

    minutes_label = Label(top_frame2, text="min od obecnego czasu.", font=("Times New Roman", 10)
                          ).grid(row=0, column=4)

    apply_button = Button(top_frame2, text="OBLICZ/ODŚWIEŻ", padx=5, font=("Times New Roman", 10),
                          command=lambda: [update_variables(), window.destroy(), wallet_window()]
                          ).grid(row=0, column=5)

    date_label = Label(top_frame3, height=2, padx=10, text="Zmiana wartości została policzona w przedziale:",
                       font=("Times New Roman", 10)).grid(column=0, row=0)
    date_now_label = Label(top_frame3, height=2, padx=10, text="Od: " + str(time_now), font=("Times New Roman", 10)
                           ).grid(column=1, row=0)
    date_then_label = Label(top_frame3, height=2, padx=10, text="Do: " + str(time_then), font=("Times New Roman", 10)
                            ).grid(column=2, row=0)

    btc_amount = Label(btc_frame, padx=10, text="Ilość zasobów:\n" + str(L6funkcje.suma_btc())
                       ).grid(column=1, row=0)
    xrp_amount = Label(xrp_frame, padx=10, text="Ilość zasobów:\n" + str(L6funkcje.suma_xrp())
                       ).grid(column=1, row=0)
    ltc_amount = Label(ltc_frame, padx=10, text="Ilość zasobów:\n" + str(L6funkcje.suma_ltc())
                       ).grid(column=1, row=0)
    eth_amount = Label(eth_frame, padx=10, text="Ilość zasobów:\n" + str(L6funkcje.suma_eth())
                       ).grid(column=1, row=0)
    bch_amount = Label(bch_frame, padx=10, text="Ilość zasobów:\n" + str(L6funkcje.suma_bch())
                       ).grid(column=1, row=0)

    btc_val = Label(btc_frame, padx=10, text="Wartość posiadanej waluty:\n" + str(
        round(L6funkcje.suma_btc()*btc_last, 2)) + " USD"
                       ).grid(column=2, row=0)
    xrp_val = Label(xrp_frame, padx=10, text="Wartość posiadanej waluty:\n" + str(
        round(L6funkcje.suma_xrp()*xrp_last, 5)) + " USD"
                       ).grid(column=2, row=0)
    ltc_val = Label(ltc_frame, padx=10, text="Wartość posiadanej waluty:\n" + str(
        round(L6funkcje.suma_ltc()*ltc_last, 2)) + " USD"
                       ).grid(column=2, row=0)
    eth_val = Label(eth_frame, padx=10, text="Wartość posiadanej waluty:\n" + str(
        round(L6funkcje.suma_eth()*eth_last, 2)) + " USD"
                       ).grid(column=2, row=0)
    bch_val = Label(bch_frame, padx=10, text="Wartość posiadanej waluty:\n" + str(
        round(L6funkcje.suma_bch()*bch_last, 2)) + " USD"
                       ).grid(column=2, row=0)

    btc_war_proc = Label(btc_frame, padx=10, text="Zmiana procentowa wartości:\n" + str(format(btc[3], '+')) + " %"
                         ).grid(column=3, row=0)
    xrp_war_proc = Label(xrp_frame, padx=10, text="Zmiana procentowa wartości:\n" + str(format(xrp[3], '+')) + " %"
                         ).grid(column=3, row=0)
    ltc_war_proc = Label(ltc_frame, padx=10, text="Zmiana procentowa wartości:\n" + str(format(ltc[3], '+')) + " %"
                         ).grid(column=3, row=0)
    eth_war_proc = Label(eth_frame, padx=10, text="Zmiana procentowa wartości:\n" + str(format(eth[3], '+')) + " %"
                         ).grid(column=3, row=0)
    bch_war_proc = Label(bch_frame, padx=10, text="Zmiana procentowa wartości:\n" + str(format(bch[3], '+')) + " %"
                         ).grid(column=3, row=0)

    btc_war = Label(btc_frame, padx=10, text="Zmiana wartości portfela:\n" + str(
        format(round(btc[2] * L6funkcje.suma_btc(), 2), '+')) + " USD"
                    ).grid(column=4, row=0)
    xrp_war = Label(xrp_frame, padx=10, text="Zmiana wartości portfela:\n" + str(
        format(round(xrp[2] * L6funkcje.suma_xrp(), 5), '+')) + " USD"
                    ).grid(column=4, row=0)
    ltc_war = Label(ltc_frame, padx=10, text="Zmiana wartości portfela:\n" + str(
        format(round(ltc[2] * L6funkcje.suma_ltc(), 2), '+')) + " USD"
                    ).grid(column=4, row=0)
    eth_war = Label(eth_frame, padx=10, text="Zmiana wartości portfela:\n" + str(
        format(round(eth[2] * L6funkcje.suma_eth(), 2), '+')) + " USD"
                    ).grid(column=4, row=0)
    bch_war = Label(bch_frame, padx=10, text="Zmiana wartości portfela:\n" + str(
        format(round(bch[2] * L6funkcje.suma_bch(), 2), '+')) + " USD"
                    ).grid(column=4, row=0)

    add_button1 = Button(btc_frame, text="Dodaj zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.add_btc(window), window.destroy(), wallet_window()]
                         ).grid(column=9, row=0)
    add_button2 = Button(xrp_frame, text="Dodaj zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.add_xrp(window), window.destroy(), wallet_window()]
                         ).grid(column=9, row=0)
    add_button3 = Button(ltc_frame, text="Dodaj zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.add_ltc(window), window.destroy(), wallet_window()]
                         ).grid(column=9, row=0)
    add_button4 = Button(eth_frame, text="Dodaj zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.add_eth(window), window.destroy(), wallet_window()]
                         ).grid(column=9, row=0)
    add_button5 = Button(bch_frame, text="Dodaj zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.add_bch(window), window.destroy(), wallet_window()]
                        ).grid(column=9, row=0)

    del_button1 = Button(btc_frame, text="Usuń zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.del_btc(window), window.destroy(), wallet_window()]
                         ).grid(column=10, row=0)
    del_button2 = Button(xrp_frame, text="Usuń zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.del_xrp(window), window.destroy(), wallet_window()]
                         ).grid(column=10, row=0)
    del_button3 = Button(ltc_frame, text="Usuń zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.del_ltc(window), window.destroy(), wallet_window()]
                         ).grid(column=10, row=0)
    del_button4 = Button(eth_frame, text="Usuń zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.del_eth(window), window.destroy(), wallet_window()]
                         ).grid(column=10, row=0)
    del_button5 = Button(bch_frame, text="Usuń zasób...", width=10, padx=2, pady=2, font=("Times New Roman", 12),
                         command=lambda: [L6funkcje.del_bch(window), window.destroy(), wallet_window()]
                         ).grid(column=10, row=0)
    suma = (L6funkcje.suma_btc() * btc_last) + (L6funkcje.suma_eth() * eth_last) + (L6funkcje.suma_xrp() * xrp_last) + \
           (L6funkcje.suma_ltc() * ltc_last) + (L6funkcje.suma_bch() * bch_last)
    suma = round(suma, 2)

    zmiana_sumy = (btc[2] * L6funkcje.suma_btc()) + (xrp[2] * L6funkcje.suma_xrp()) + (ltc[2] * L6funkcje.suma_ltc()) + \
                  (eth[2] * L6funkcje.suma_eth()) + (bch[2] * L6funkcje.suma_bch())
    zmiana_sumy = round(zmiana_sumy, 2)

    if (suma == 0) or (suma-zmiana_sumy == 0):
        proc_s = 0
    else:
        proc_s = ((suma / (suma - zmiana_sumy)) - 1) * 100
        proc_s = round(proc_s, 2)

    sum_label1 = Label(sum_frame, text="Suma wartości posiadanych walut:\n" + str(suma) + " USD", padx=10
                       ).grid(row=0, column=0)
    sum_label2 = Label(sum_frame, text="Zmiana sumy wartości posiadanych walut:\n" + str(format(zmiana_sumy,'+'))
                                       + " USD", padx=10).grid(row=0, column=1)
    sum_label3 = Label(sum_frame, text="Procentowa zmiana sumy wartości posiadanych walut:\n" + str(format(proc_s, '+'))
                                       + " %", padx=10).grid(row=0, column=2)

    exit_button2 = Button(bottom_frame, text="WYJDŹ", padx=2, pady=2, font=("Times New Roman", 20),
                          command=window.destroy).grid(column=2, row=0, columnspan=2)

    window.mainloop()


def history_window():
    window = Toplevel()
    window.title("Historia")
    window.geometry('+0+0')

    frame1 = Frame(window)
    frame1.grid(row=0)
    frame2 = Frame(window)
    frame2.grid(row=1)

    currency = StringVar(window)
    currency.set("btc")
    currency_change = OptionMenu(frame2, currency, "btc", "xrp", "ltc", "eth", "bch")
    currency_change.grid(row=0)

    title_label = Label(frame1, text='Historia dodawania i usuwania ilości danej waluty:').grid(row=0)

    text = scrolledtext.ScrolledText(frame1, height=20, width=43)
    text.grid(row=1)
    currency.trace('w', lambda x, options=currency, txt=text: L6funkcje.set_history(currency, text))
    L6funkcje.set_history(currency, text)

    exit_button3 = Button(frame2, text="WYJDŹ", padx=2, pady=2, font=("Times New Roman", 20),
                          command=window.destroy).grid(row=1)
    window.mainloop()


def data_window():
    window = Toplevel()
    window.title("Dane")
    window.geometry('+0+0')

    btc_tick, xrp_tick, ltc_tick, eth_tick, bch_tick = L6funkcje.bitstamp_ticker()

    top_frame = Frame(window)
    top_frame.grid(row=0)
    btc_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='BTC', font=("Arial", 10))
    btc_frame.grid(row=1)
    xrp_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='XRP', font=("Arial", 10))
    xrp_frame.grid(row=2)
    eth_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='ETH', font=("Arial", 10))
    eth_frame.grid(row=3)
    ltc_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='LTC', font=("Arial", 10))
    ltc_frame.grid(row=4)
    bch_frame = LabelFrame(window, bd=5, relief='groove', padx=4, pady=4, text='BCH', font=("Arial", 10))
    bch_frame.grid(row=5)
    bottom_frame = Frame(window)
    bottom_frame.grid(row=6)

    time_label = Label(top_frame, text='Data i czas pobrania danych: ' + str(
        datetime.fromtimestamp(int(btc_tick['timestamp']))), padx=10, font=("Arial", 15)).grid(row=0)

    price_label1 = Label(btc_frame, text='Cena jednostkowa:\n' + btc_tick['last'] + ' USD', padx=10, font=("Arial", 10)
                         ).grid(row=0, column=0)
    price_label2 = Label(xrp_frame, text='Cena jednostkowa:\n' + xrp_tick['last'] + ' USD', padx=10, font=("Arial", 10)
                         ).grid(row=0, column=0)
    price_label3 = Label(eth_frame, text='Cena jednostkowa:\n' + eth_tick['last'] + ' USD', padx=10, font=("Arial", 10)
                         ).grid(row=0, column=0)
    price_label4 = Label(ltc_frame, text='Cena jednostkowa:\n' + ltc_tick['last'] + ' USD', padx=10, font=("Arial", 10)
                         ).grid(row=0, column=0)
    price_label5 = Label(bch_frame, text='Cena jednostkowa:\n' + bch_tick['last'] + ' USD', padx=10, font=("Arial", 10)
                         ).grid(row=0, column=0)

    price2_label1 = Label(btc_frame, text='Najwyższa cena w ciągu 24h:\n' + btc_tick['high'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=1)
    price2_label2 = Label(xrp_frame, text='Najwyższa cena w ciągu 24h:\n' + xrp_tick['high'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=1)
    price2_label3 = Label(eth_frame, text='Najwyższa cena w ciągu 24h:\n' + eth_tick['high'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=1)
    price2_label4 = Label(ltc_frame, text='Najwyższa cena w ciągu 24h:\n' + ltc_tick['high'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=1)
    price2_label5 = Label(bch_frame, text='Najwyższa cena w ciągu 24h:\n' + bch_tick['high'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=1)

    price3_label1 = Label(btc_frame, text='Najniższa cena w ciągu 24h:\n' + btc_tick['low'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=2)
    price3_label2 = Label(xrp_frame, text='Najniższa cena w ciągu 24h:\n' + xrp_tick['low'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=2)
    price3_label3 = Label(eth_frame, text='Najniższa cena w ciągu 24h:\n' + eth_tick['low'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=2)
    price3_label4 = Label(ltc_frame, text='Najniższa cena w ciągu 24h:\n' + ltc_tick['low'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=2)
    price3_label5 = Label(bch_frame, text='Najniższa cena w ciągu 24h:\n' + bch_tick['low'] + ' USD', padx=10,
                          font=("Arial", 10)).grid(row=0, column=2)

    volume_label1 = Label(btc_frame, text='Suma ilość waluty we wszystkich transakcjach w ciągu 24 h:\n'
                                    + btc_tick['volume'], padx=10, font=("Arial", 10)).grid(row=0, column=3)
    volume_label2 = Label(xrp_frame, text='Suma ilość waluty we wszystkich transakcjach w ciągu 24 h:\n'
                                    + xrp_tick['volume'], padx=10, font=("Arial", 10)).grid(row=0, column=3)
    volume_label3 = Label(eth_frame, text='Suma ilość waluty we wszystkich transakcjach w ciągu 24 h:\n'
                                    + eth_tick['volume'], padx=10, font=("Arial", 10)).grid(row=0, column=3)
    volume_label4 = Label(ltc_frame, text='Suma ilość waluty we wszystkich transakcjach w ciągu 24 h:\n'
                                    + ltc_tick['volume'], padx=10, font=("Arial", 10)).grid(row=0, column=3)
    volume_label5 = Label(bch_frame, text='Suma ilość waluty we wszystkich transakcjach w ciągu 24 h:\n'
                                    + bch_tick['volume'], padx=10, font=("Arial", 10)).grid(row=0, column=3)

    price4_label1 = Label(btc_frame, text='Stosunek pierwszej ceny do obecnej ceny w ciągu 24h:\n'
                    + str(format(round(((float(btc_tick['last']) / float(btc_tick['open']) - 1) * 100), 2), '+')) +
                    ' %', padx=10, font=("Arial", 10)).grid(row=0, column=4)
    price4_label2 = Label(xrp_frame, text='Stosunek pierwszej ceny do obecnej ceny w ciągu 24h:\n'
                    + str(format(round(((float(xrp_tick['last']) / float(xrp_tick['open']) - 1) * 100), 2), '+')) +
                    ' %', padx=10, font=("Arial", 10)).grid(row=0, column=4)
    price4_label3 = Label(eth_frame, text='Stosunek pierwszej ceny do obecnej ceny w ciągu 24h:\n'
                    + str(format(round(((float(eth_tick['last']) / float(eth_tick['open']) - 1) * 100), 2), '+')) +
                    ' %', padx=10, font=("Arial", 10)).grid(row=0, column=4)
    price4_label4 = Label(ltc_frame, text='Stosunek pierwszej ceny do obecnej ceny w ciągu 24h:\n'
                    + str(format(round(((float(ltc_tick['last']) / float(ltc_tick['open']) - 1) * 100), 2), '+')) +
                    ' %', padx=10, font=("Arial", 10)).grid(row=0, column=4)
    price4_label5 = Label(bch_frame, text='Stosunek pierwszej ceny do obecnej ceny w ciągu 24h:\n'
                    + str(format(round(((float(bch_tick['last']) / float(bch_tick['open']) - 1) * 100), 2), '+')) +
                    ' %', padx=10, font=("Arial", 10)).grid(row=0, column=4)

    exit_button4 = Button(bottom_frame, text="WYJDŹ", padx=2, pady=2, font=("Times New Roman", 20),
                          command=window.destroy).grid(row=0, column=1)
    refresh_button = Button(bottom_frame, text="ODŚWIEŻ", padx=2, pady=2, font=("Times New Roman", 20),
                            command=lambda: [window.destroy(), data_window()]).grid(row=0, column=0)
    window.mainloop()


def main():
    open('btc.csv', 'a')
    open('eth.csv', 'a')
    open('ltc.csv', 'a')
    open('xrp.csv', 'a')
    open('bch.csv', 'a')
    root = Tk()
    root.title("LAB 6")
    root.geometry('+0+0')

    global btc_check, xrp_check, eth_check, ltc_check, bch_check
    btc_check = IntVar()
    btc_check.set(1)
    xrp_check = IntVar()
    xrp_check.set(1)
    eth_check = IntVar()
    eth_check.set(1)
    ltc_check = IntVar()
    ltc_check.set(1)
    bch_check = IntVar()
    bch_check.set(1)

    global hours, minutes
    hours = IntVar()
    minutes = IntVar()
    hours.set(1)
    minutes.set(0)

    global btc, xrp, ltc, eth, bch, time_now, time_then
    btc, xrp, ltc, eth, bch, time_now, time_then = L6funkcje.bitstamp_gain(hours.get(), minutes.get())

    global btc_last, xrp_last, ltc_last, eth_last, bch_last
    btc_last, xrp_last, ltc_last, eth_last, bch_last = L6funkcje.currency_current_price()

    wallet_button = Button(root, text="Portfel", padx=2, pady=2, font=("Arial", 15),
                           command=wallet_window).grid(row=0)
    history_button = Button(root, text="Historia\nWpłat i Wypłat", padx=2, pady=2, font=("Arial", 15),
                            command=history_window).grid(row=1)
    data_button = Button(root, text="Dane Walut", padx=2, pady=2, font=("Arial", 15),
                         command=data_window).grid(row=2)
    exit_button = Button(root, text="Wyjdź", padx=2, pady=2, font=("Arial", 15),
                         command=root.destroy).grid(row=3)
    root.mainloop()


main()
