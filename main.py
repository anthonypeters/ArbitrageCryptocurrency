# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of Bellman-Ford Algorithm to visualize arbitrage opportunities in Python/Flask

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
from Arbitrage import Arbitrage
from Node import Node
from Edge import Edge
import numpy as np
from firebase import firebase

#Loads in an Exchange
#Loads in currency_pairs and appends them to a list
exchange = ccxt.bitmex()
currency_pairs = []
for n in exchange.load_markets():
    currency_pairs.append(n)
print(currency_pairs)

#Create a node for every currency pair with BTC/USD being the start vertex
for n in currency_pairs:
    startVertex = 'BTC/USD'
    node = new Node(n)
    pass

#Create an edge weight for each node connection
for each Node:
    edge = Edge(n, n+1)
    Node(n).adjacenciesList.append(Edge(n))

#Call arbitrage function shortest path
arbitrage = Arbitrage()
arbitrage.shortestPath()













'''

firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", "")


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
    result = firebase.post('/crypto-arbitrage-6575e/Exchanges', elem)
    print(elem)


'''
