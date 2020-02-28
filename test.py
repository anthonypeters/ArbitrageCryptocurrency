from firebase import firebase
firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", None)
result = firebase.get("/crypto-arbitrage-6575e/Team", '')
print(result)


data ={
    'Name' : 'Franz Nastor',
    'Email' : 'frnz.nstr@gmail.com'
}

result = firebase.post('/crypto-arbitrage-6575e/Team', data)
print(result)

result2 = firebase.get("/crypto-arbitrage-6575e/Team", '')
print(result2)