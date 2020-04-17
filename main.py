# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of Bellman-Ford Algorithm to visualize arbitrage opportunities in Python/Flask

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
from firebase import firebase


def replace_currency(substring, list):
    for n in list:
        list.sort()
        if substring in str(n):
            list.remove(n)


def cycles_algorithm(Graph):
    firstNode = None
    lastNode = None
    nodes = list(Graph.nodes)
    perm = permutations(nodes, 2)
    permutationsList = list(perm)
    cycles = []

    for i in permutationsList:
        a,b = i
        if (a != b):
            cycles.append((a, b))

    print(cycles)
    print(len(cycles))
    return cycles


def algorithm(Graph, cycles):
    x = 0
    firstNode = None
    secondNode = None
    thirdNode = None
    lastNode = None
    nodes = list(Graph.nodes)
    valueList = []

    while x < len(nodes)-1:
        for cycle in cycles:
            a, b = cycle
            firstNode = nodes[x]
            secondNode = a
            thirdNode = b
            lastNode = nodes[x]

            if firstNode != a and lastNode != b:
                dict = Graph.get_edge_data(firstNode, secondNode, 0)
                dict2 = Graph.get_edge_data(secondNode, thirdNode, 0)
                dict3 = Graph.get_edge_data(thirdNode, lastNode, 0)

                if dict != 0 and dict2 != 0 and dict3 != 0:
                    value = float(1.0 * dict['weight'] * dict2['weight'] * dict3['weight'])
                    if value > 1.01:
                        valueList.append(value)

        x+=1
    print(len(valueList))
    valueList.sort(reverse=True)
    print(valueList)
    return valueList


# Loads in our Exchange
# Loads in currency_pairs and adds them to a list with BTC/USD as last item
# Creates Graph
exchange = ccxt.binanceus()
exchange.load_markets()
currency_pairs = exchange.symbols
currency_pairs.sort()
G = nx.DiGraph()

# Loads ask and bid price holder for the exchange and currency pairs
ask = np.zeros(5)
bid = np.zeros(5)

# Replace currency in the list function
substring = 'USDT'
substring2 = 'BUSD'
substring3 = '/BTC'

replace_currency(substring, currency_pairs)
replace_currency(substring2, currency_pairs)
replace_currency(substring3, currency_pairs)

# Creates and appends edges to the graph with a calculated weight
n = 0
j = 0

while n < len(currency_pairs)-1:

    book = exchange.fetch_order_book(currency_pairs[n], 5)
    ask = book['asks'][0][0]

    while j < len(currency_pairs)-1:
        book = exchange.fetch_order_book(currency_pairs[j], 5)
        bid = book['bids'][0][0]
        weight = ask / bid
        edge = [currency_pairs[n], currency_pairs[j], weight]
        if edge[0] != edge[1]:
            G.add_edge(edge[0], edge[1], weight=edge[2])
        j += 1

    n += 1
    j = 0


G.add_nodes_from(currency_pairs)
print(G.nodes)
print(G.number_of_nodes())
print(G.edges.data())
print(G.number_of_edges())

#nx.draw_circular(G)
#plt.show()

cycles = cycles_algorithm(G)
algorithm(G, cycles)
#firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", "")







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
