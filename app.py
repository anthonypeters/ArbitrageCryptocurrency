from firebase import firebase
firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/")

data ={
    'Name' : 'Anthony Peters',
    'Email' : 'anthonyypeterss@gmail.com'
}

result = firebase.post('/crypto-arbitrage-6575e/Team', data)
print(result)

