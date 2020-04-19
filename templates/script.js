var database;

var firebaseConfig = {
    apiKey: "AIzaSyCdleI0nwtYWRkap5DlmIa0T3fbCFplKQI",
    authDomain: "crypto-arbitrage-6575e.firebaseapp.com",
    databaseURL: "https://crypto-arbitrage-6575e.firebaseio.com",
    projectId: "crypto-arbitrage-6575e",
    storageBucket: "crypto-arbitrage-6575e.appspot.com",
    messagingSenderId: "786238497188",
    appId: "1:786238497188:web:320b4346088c6f41dca131",
    measurementId: "G-CP5N8HVL5Q"
  };

firebase.initializeApp(firebaseConfig);

database = firebase.database()

for (var key in db.val()) {
    // => do what you need
}

