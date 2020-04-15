# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of Bellman-Ford Algorithm to visualize arbitrage opportunities in Python/Flask

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np
import math
import networkx as nx
from Arbitrage import Arbitrage
from firebase import firebase


# Loads in our Exchange
# Loads in currency_pairs and adds them to a list with BTC/USD as last item
exchange = ccxt.binanceus()
exchange.load_markets()
currency_pairs = exchange.symbols



# Replace currency in the list function
substring = 'USDT'
substring2 = 'BUSD'

def replace_currency(substring, list):
    for n in list:
        if substring in str(n):
            list.remove(n)

replace_currency(substring, currency_pairs)
replace_currency(substring2, currency_pairs)



# Loads ask and bid price for the exchange and currency pairs
# Creates Graph and adds each currency pair to a node in the graph
ask = np.zeros((len(currency_pairs)))
bid = np.zeros((len(currency_pairs)))

G = nx.MultiDiGraph()
G.add_nodes_from(currency_pairs)



# Creates and appends edges to the graph with a calculated weight
edges = []
weights = []
n = 0
j = 1
while n < len(currency_pairs)-1:

    book = exchange.fetch_order_book(currency_pairs[n], 5)
    ask = book['asks'][0][0]

    while j < len(currency_pairs)-1:
        book = exchange.fetch_order_book(currency_pairs[j], 5)
        bid = book['bids'][0][0]
        weight = ask / bid
        weight = (-(math.log(weight)))
        edge = [currency_pairs[n], currency_pairs[j]]
        G.add_edge(edge[0], edge[1], weight)
        j += 1

    n += 1
    j = 1



print(G.nodes)
print(G.edges)
print(len(G.nodes))
print(len(G.edges))


'''
def algorithm(Graph):
    startVertex = G.nodes['BTC/USD']
    vertexList = G.nodes
    edgeList = G.edges

    for i in range(0, len(vertexList) - 1):
        for edge in edgeList:

            u = edge.startVertex
            v = edge.targetvertex
            newDistance = edge[0]

            if newDistance < 0:
                v.minDistance = newDistance
                v.predecessor = u;

    for edge in edgeList:
        if self.hasCycle(edge):
            print("Negative cycle detected")
            Arbitrage.HAS_CYCLE = True
        return
'''





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
