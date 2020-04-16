# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of Bellman-Ford Algorithm to visualize arbitrage opportunities in Python/Flask

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
from firebase import firebase


# Loads in our Exchange
# Loads in currency_pairs and adds them to a list with BTC/USD as last item
exchange = ccxt.binanceus()
exchange.load_markets()
currency_pairs = exchange.symbols
currency_pairs.sort()



# Replace currency in the list function
substring = 'USDT'
substring2 = 'BUSD'
substring3 = '/BTC'


def replace_currency(substring, list):
    for n in list:
        if substring in str(n):
            list.remove(n)

replace_currency(substring, currency_pairs)
replace_currency(substring2, currency_pairs)
replace_currency(substring3, currency_pairs)



# Loads ask and bid price for the exchange and currency pairs
# Creates Graph and adds each currency pair to a node in the graph
ask = np.zeros((len(currency_pairs)))
bid = np.zeros((len(currency_pairs)))

G = nx.DiGraph()
G.add_nodes_from(currency_pairs)
print(G.nodes)
print(G.number_of_nodes())

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
        weight = (-(math.log(weight)))
        edge = [currency_pairs[n], currency_pairs[j], weight]
        if weight > 0:
            G.add_edge(edge[0], edge[1], weight = edge[2])
        j += 1

    n += 1
    j = 0


print(G.edges.data())
print(G.number_of_edges())

#nx.draw(G)
#plt.show()


def algorithm(Graph):
    x = 0
    y = 0
    nodes = list(Graph.nodes)
    nextNode = nodes[y]
    totalWeight = 0

    while x < len(Graph.nodes)-1:
        startNode = nodes[x]

        while y < len(Graph.nodes)-1:
            dict = Graph.get_edge_data(startNode, nextNode, 0)
            if dict != 0:
                print(dict['weight'])
                totalWeight += dict['weight']
                print(totalWeight)
            startNode = nextNode
            nextNode = nodes[y+1]
            y += 1
        x += 1
        y = 0

algorithm(G)


'''
for each node in the graph
    call create cycles function that creates a cycle for every pair

def create_cycles(G):
    sets starting node
    then for every other node in the list
    create cycle = (node1, node2, node3, node1, total weight)
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
