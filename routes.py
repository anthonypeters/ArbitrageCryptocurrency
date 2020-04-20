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
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        nodes = db.child("crypto-arbitrage-6575e").child("Nodes")
        node_names = nodes.val()

        for n in node_names:
            #TODO save option selection from drop down list into variable and use it here
            if (option_selection == n):
                opportunities = db.child("crypto-arbitrage-6575e").child("Opportunities").child().get(1)
                results = opportunities.val()
                response = json.dumps(str(results), sort_keys=True, indent=4, separators=(',', ': '))
                return render_template('index.html', response=response)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
