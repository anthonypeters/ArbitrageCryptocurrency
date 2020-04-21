from pyrebase import pyrebase
from flask import *

config = {
    "apiKey": "AIzaSyCdleI0nwtYWRkap5DlmIa0T3fbCFplKQI",
    "authDomain": "crypto-arbitrage-6575e.firebaseapp.com",
    "databaseURL": "https://crypto-arbitrage-6575e.firebaseio.com",
    "projectId": "crypto-arbitrage-6575e",
    "storageBucket": "crypto-arbitrage-6575e.appspot.com",
    "messagingSenderId": "786238497188",
    "appId": "1:786238497188:web:320b4346088c6f41dca131",
    "measurementId": "G-CP5N8HVL5Q"
}

firebase2 = pyrebase.initialize_app(config)

db = firebase2.database()

app = Flask(__name__)


#TODO finalize flask with working opportunities list
'''
@app.route('/', methods=['GET'])
def dropdown():
    currencies = ['Red', 'Blue', 'Black']
    return render_template(test.html, colors = colors)
'''



@app.route('/', methods=['GET', 'POST'])
def home():
    currencies = []
    items = db.child("crypto-arbitrage-6575e").child("Nodes").get()
    for n in items.each():
        result = n.val()
        currencies.append(result)

    if request.method == "GET":
        return render_template('index.html', currencies=currencies)

    if request.method == "POST":
        currency = request.form['currency']
        related_opportunities = []
        all_opportunities = db.child("crypto-arbitrage-6575e").child("Opportunities").child().get()

        for n in all_opportunities.each():
            opportunities_list = n.val()

            for opportunities in opportunities_list:
                if currency == opportunities[1]:
                    related_opportunities.append(opportunities)

        return render_template('index.html', currencies=currencies, opportunities_list=related_opportunities)


if __name__ == '__main__':
    app.run(port=8000)

