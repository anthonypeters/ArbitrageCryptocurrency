from firebase import firebase
firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/")

data ={
    'Name' : 'Collin Jones',
    'Email' : 'cjhockey65@gmail.com'
}

result = firebase.post('/crypto-arbitrage-6575e/Team', data)
print(result)