# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of sorting algorithm
# Use of Bellman-Ford Algorithm or Dijkstra's Algorithm
# Depth First Search + Breadth First Search


# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np
from math import log

# Non compatible exchanges: ['binanceje', 'braziliex', 'btcchina', 'bitfinex', 'bitfinex2', 'bittrex', 'chilebit', 'btcturk',
# 'fcoinjp', 'coinmarketcap', 'gateio', 'huobipro', 'huobiru', 'indodax', 'btctradeua', 'zaif', 'zb', 'yobit', 'xbtce', '_1btcxe',
# 'bibox', 'bitmex', 'bitstamp1', 'bitz', 'poloniex', 'theocean', 'btcalpha', 'fybse', 'allcoin', 'upbit']

exchanges = ['acx', 'adara', 'anxpro', 'bcex', 'bequant', 'bigone', 'binance',
             'binanceus', 'bit2c', 'bitbank', 'bitbay', 'bitflyer', 'bitforex', 'bithumb', 'bitkk', 'bitlish',
             'bitmart', 'bitmax', 'bitso', 'bitstamp', 'bl3p', 'bleutrade', 'btcbox', 'btcmarkets', 'btctradeim',
             'buda', 'bw', 'bytetrade', 'cex', 'cobinhood', 'coinbase', 'coinbaseprime', 'coinbasepro',
             'coincheck', 'coinegg', 'coinex', 'coinfalcon', 'coinfloor', 'coingi',  'coinmate', 'coinone',
             'coinspot', 'coolcoin', 'coss', 'crex24', 'deribit', 'digifinex', 'dsx', 'exmo', 'exx', 'fcoin',
             'flowbtc', 'foxbit', 'ftx', 'gemini', 'hitbtc', 'hitbtc2', 'ice3x', 'idex', 'independentreserve',
             'itbit', 'kkex', 'kraken', 'kucoin', 'kuna', 'lakebtc', 'latoken', 'lbank', 'liquid', 'livecoin',
             'luno', 'lykke', 'mercado', 'mixcoins', 'oceanex', 'okcoincny', 'okcoinusd', 'okex', 'okex3',
             'paymium', 'rightbtc', 'southxchange', 'stex', 'stronghold', 'surbitcoin', 'therock', 'tidebit',
             'tidex', 'timex', 'vaultoro', 'vbtc', 'whitebit']

currency_pairs = ["ADA/BTC", "BCH/BTC", "BTG/BTC", "BTS/BTC", "CLAIM/BTC", "DASH/BTC", "DOGE/BTC", "EDO/BTC", "EOS/BTC",
                  "ETC/BTC","ETH/BTC", "FCT/BTC", "ICX/BTC", "IOTA/BTC", "LSK/BTC", "LTC/BTC", "MAID/BTC", "NEO/BTC",
                  "OMG/BTC", "QTUM/BTC", "STR/BTC", "TRX/BTC","VEN/BTC", "XEM/BTC", "XLM/BTC", "XMR/BTC", "XRP/BTC", "ZEC/BTC",
                  "ADA/BTC"]
                  #"BCH/USD", "BTG/USD", "BTS/USD", "CLAIM/USD", "DASH/USD", "DOGE/USD", "EDO/USD", "EOS/USD",
                  #"ETC/USD", "ETH/USD", "FCT/USD", "ICX/USD", "IOTA/USD", "LSK/USD", "LTC/USD", "MAID/USD", "NEO/USD",
                  #"OMG/USD", "QTUM/USD", "STR/USD", "TRX/USD", "VEN/USD", "XEM/USD", "XLM/USD", "XMR/USD", "XRP/USD",
                  #"ZEC/USD"]

fee = 0.25

clients = [getattr(ccxt, e.lower())() for e in exchanges]

ask = np.zeros((len(currency_pairs), len(clients)))
bid = np.zeros((len(currency_pairs), len(clients)))

for row, symbol in enumerate(currency_pairs):
    for col, client in enumerate(clients):

        try:
            book = client.fetch_order_book(symbol)
            ask[row, col] = book['asks'][0][0]
            bid[row, col] = book['bids'][0][0]
        except:
            pass

opportunities = []

for i, symbol in enumerate(currency_pairs):
    for p1, exchange1 in enumerate(exchanges):
        for p2, exchange2 in enumerate(exchanges):
            roi = 0
            if p1 != p2 and (ask[i, p1] > 0):
                roi = ((bid[i, p2] * (1 - fee / 100)) / (ask[i, p1] * (1 + fee / 100)) - 1) * 100

                if roi > 0:
                    opportunities.append([symbol, exchange1, ask[i, p1], exchange2, bid[i, p2], round(roi, 2)])

print("Number of profitable opportunities:", len(opportunities))

opportunities = sorted(opportunities, reverse = True, key=lambda ele: ele[5])

for elem in opportunities:
    print(elem)


#Given an exchange calculate arbitrage opportunities
# def arbitrage(exchange):
#Fetch currency pairs on the exchange
#     currencyPairs = exchange.fetchCurrencies()
#import real time exchange rates for the different currency pairs
#     currencyPairMatrix =
#Create a graph with the edge weights as the -log of the exchange rate and nodes as the currencies
#     graph = [[-log(edge) for edge in row] for row in graph]
#.... Functionality

