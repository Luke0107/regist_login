from firebase import firebase
url = 'https://python-d2cab-default-rtdb.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)
fdb.delete('/', '')