# Arbitrage Cryptocurrency
# Use of Bellman-Ford Algorithm or Dijkstra's Algorithm
# Use of CCXT Library
# Use of sorting algorithm

# Anthony Peters, Franz Nastor, Peter Radev, Jack Hudanick, Tim Abbenhaus, Collin Jones

import ccxt
import numpy as np

# Non compatible exchanges: ['binanceje', 'braziliex', 'btcchina', 'bitfinex', 'bitfinex2', 'bittrex', 'chilebit', 'btcturk',
# 
exchanges = ['_1btcxe', 'acx', 'adara', 'allcoin', 'anxpro', 'bcex', 'bequant', 'bibox', 'bigone',
             'binance',  'binanceus', 'bit2c', 'bitbank', 'bitbay', 'bitflyer', 'bitforex',
             'bithumb', 'bitkk', 'bitlish', 'bitmart', 'bitmax', 'bitmex', 'bitso', 'bitstamp', 'bitstamp1', 'bitz', 'bl3p', 'bleutrade', 'btcalpha', 'btcbox',
              'btcmarkets', 'btctradeim', 'btctradeua', 'buda', 'bw', 'bytetrade', 'cex',
             'cobinhood', 'coinbase', 'coinbaseprime', 'coinbasepro', 'coincheck', 'coinegg', 'coinex',
             'coinfalcon', 'coinfloor', 'coingi', 'coinmarketcap', 'coinmate', 'coinone', 'coinspot', 'coolcoin', 'coss',
             'crex24', 'deribit', 'digifinex', 'dsx', 'exmo', 'exx', 'fcoin', 'fcoinjp', 'flowbtc', 'foxbit', 'ftx', 'fybse',
             'gateio', 'gemini', 'hitbtc', 'hitbtc2', 'huobipro', 'huobiru', 'ice3x', 'idex', 'independentreserve', 'indodax',
             'itbit', 'kkex', 'kraken', 'kucoin', 'kuna', 'lakebtc', 'latoken', 'lbank', 'liquid', 'livecoin', 'luno', 'lykke',
             'mercado', 'mixcoins', 'oceanex', 'okcoincny', 'okcoinusd', 'okex', 'okex3', 'paymium', 'poloniex', 'rightbtc',
             'southxchange', 'stex', 'stronghold', 'surbitcoin', 'theocean', 'therock', 'tidebit', 'tidex', 'timex', 'upbit',
             'vaultoro', 'vbtc', 'whitebit', 'xbtce', 'yobit', 'zaif', 'zb']
fee = 0.25

clients = [getattr(ccxt, e.lower())() for e in exchanges]

currency_pairs = ["ADA/BTC", "BCH/BTC", "BTG/BTC", "BTS/BTC", "CLAIM/BTC", "DASH/BTC", "DOGE/BTC", "EDO/BTC", "EOS/BTC",
           "ETC/BTC","ETH/BTC", "FCT/BTC", "ICX/BTC", "IOTA/BTC", "LSK/BTC", "LTC/BTC", "MAID/BTC", "NEO/BTC",
           "OMG/BTC", "QTUM/BTC", "STR/BTC", "TRX/BTC","VEN/BTC", "XEM/BTC", "XLM/BTC", "XMR/BTC", "XRP/BTC", "ZEC/BTC"]

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
    for j1, exchange1 in enumerate(exchanges):
        for j2, exchange2 in enumerate(exchanges):

            roi = 0
            if j1 != j2 and ask[i, j1] > 0:
                roi = ((bid[i, j2] * (1 - fee / 100)) / (ask[i, j1] * (1 + fee / 100)) - 1) * 100

                if roi > 0:
                    opportunities.append([symbol, exchange1, ask[i, j1], exchange2, bid[i, j2], round(roi, 2)])

print("Number of profitable opportunities:", len(opportunities))
print(opportunities)
