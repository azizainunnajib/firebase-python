import pyrebase
import requests
import json
from jsonmerge import Merger
#cara run di MVS, environment setting python 3.6. tekan shift+alt+f5., susah beut dapatnya.

def getData(child):

    config = {
      "apiKey": "AIzaSyD7QFqyZ_kxfJFg9kaGHrgh7dY43d8ZHAg",
      "authDomain": "my-project-1479543973833.firebaseapp.com",
      "databaseURL": "https://my-project-1479543973833.firebaseio.com",
      "storageBucket": "my-project-1479543973833.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    user = auth.sign_in_with_email_and_password('azizainunnajib@gmail.com', 'FirebaseAziz1')

    db = firebase.database()
    users = db.child(child).get(user['idToken'], {})
    return users

data = {"name": {"Mortimer 'Morty' Smith", "aziz", "nama"}}
#db.child("home").push(data, user['idToken'], {})
#print(users.val())

def setData(child, data):
    config = {
      "apiKey": "AIzaSyD7QFqyZ_kxfJFg9kaGHrgh7dY43d8ZHAg",
      "authDomain": "my-project-1479543973833.firebaseapp.com",
      "databaseURL": "https://my-project-1479543973833.firebaseio.com",
      "storageBucket": "my-project-1479543973833.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    user = auth.sign_in_with_email_and_password('azizainunnajib@gmail.com', 'FirebaseAziz1')

    db = firebase.database()
    db.child(child).set(data, user['idToken'], {})

def get_nexturl(data):
    if 'next_url' in data:
        url = data['pagination']['next_url']
        print(url)
    else:
        url = None

    return url
        

r = requests.get("https://api.instagram.com/v1/tags/kucing/media/recent?access_token=3859629641.8b194ec.b551c0748aa74f1fa5dd8504dcba418b")
j = r.json()
data = json.loads(r.text)
ig_user = data.get('data')
print(j['data'])
x = j['data']
print(data)
get_nexturl(data)
#db.child("home").push(data, user['idToken'], {})

idtoken = getData('User')
print(idtoken.val())

def get_data(API):
    r = requests.get(API)
    data = json.loads(r.text)
    #f = open('result_ig.json', 'r+')
    #json.dump(data, f)
    if(get_nexturl(data) == None):
        pass
    else:
        data_temp = data
        next_url = get_nexturl(data)
        for i in range(1,30):
            req = requests.get(next_url(data_temp))
            data_temp1 = req.text
            data_temp = json.dump(data_temp, data_temp1)
    return data

schema = {
            "properties": {
                "data": {
                    "mergeStrategy": "append"
                }
            }
        }

data_real = get_data('https://api.instagram.com/v1/tags/kucing/media/recent?access_token=3859629641.8b194ec.b551c0748aa74f1fa5dd8504dcba418b')
data_real1 = get_data('https://api.instagram.com/v1/tags/malang/media/recent?access_token=3859629641.8b194ec.b551c0748aa74f1fa5dd8504dcba418b')
data_real2 = get_data('https://api.instagram.com/v1/tags/Travel/media/recent?access_token=3859629641.8b194ec.b551c0748aa74f1fa5dd8504dcba418b')
merger = Merger(schema)
result = merger.merge(data_real, data_real1)
result = merger.merge(result, data_real2)
data_real3 = {'data': data_real1, 'data1': data_real, 'data2': data_real2}
#data_real3['a'] = ['ab']
i = 0
for obj in result['data']:
    obj['key'] = i
#a = result['data'][1]
#i = 0
#a['key'] = i
#print(a)
#data_coba1 = data_real3
#for k,v in data_real3.items:
#    #obj.append('a', '4')


data_real3 = json.dumps(data_real3)
print('ini awal:  ' + data_real3)
setData("Trending", result)