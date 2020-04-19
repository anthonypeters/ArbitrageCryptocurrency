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



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        todo = request.form
        names = db.child("crypto-arbitrage-6575e").child("Opportunities").child()
        name = names.get()

        for n in names:
            if n.get(1) == todo:
                response = json.dumps(str(name), sort_keys=True, indent=4, separators=(',', ': '))
                return render_template('index.html', response=response)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
