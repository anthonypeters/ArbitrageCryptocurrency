from firebase import firebase

firebase = firebase.FirebaseApplication("https://crypto-arbitrage-6575e.firebaseio.com/", "")

data = {
    'Name': 'Peter Radev',
    'Email': 'taco@gmail.com'
}

# result = firebase.post('/crypto-arbitrage-6575e/Team', data)
# print(result)

result2 = firebase.get("/crypto-arbitrage-6575e/Team", '')
print(result2)




