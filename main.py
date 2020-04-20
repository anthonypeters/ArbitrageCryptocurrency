# Arbitrage Cryptocurrency
# Use of CCXT Library
# Use of N-Hayward Algorithm to visualize arbitrage opportunities in Python/Flask

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np
import networkx as nx
import logic
from firebase import firebase
import matplotlib.pyplot as plt


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

logic.replace_currency(substring, currency_pairs)
logic.replace_currency(substring2, currency_pairs)
logic.replace_currency(substring3, currency_pairs)

# Creates and appends edges to the graph with a calculated weight
n = 0
j = 0

while n < len(currency_pairs):

    book = exchange.fetch_order_book(currency_pairs[n], 5)
    ask = book['asks'][0][0]

    while j < len(currency_pairs):
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

#Graph = nx.draw_circular(G)
#plt.show()

firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", "")
firebase.delete('crypto-arbitrage-6575e', "Opportunities")


cycles = logic.cycles_algorithm(G)
logic.n_hayward(G, cycles)


